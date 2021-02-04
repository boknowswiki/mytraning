package main

import (
	"log"
	"os"
	"os/signal"
	"sync"
	"syscall"

	"github.com/streadway/amqp"
)

// DEFAULTGOROUTINECNT defines default goroutine pool size.
const DEFAULTGOROUTINECNT = 3

func failOnError(err error, msg string) {
	if err != nil {
		log.Fatalf("%s: %s", msg, err)
	}
}

// SubWorkerChan defines the type for subscriber worker channel.
type SubWorkerChan struct {
	mqChan  *amqp.Channel
	message []byte
}

func worker(id int, wg *sync.WaitGroup, subWorkerChan chan SubWorkerChan, stop chan int) {
	defer wg.Done()

	log.Printf("worker %v start", id)

	for {
		select {
		case msg := <-subWorkerChan:
			log.Printf("worker %v gets message %v", id, string(msg.message))

		case <-stop:
			log.Printf("stoping worker %v.", id)
			return
		}
	}

	log.Println("worker should not be here.")
}

func main() {
	var wg sync.WaitGroup
	goRoutineCnt := DEFAULTGOROUTINECNT
	subWorkerChan := make(chan SubWorkerChan, goRoutineCnt)
	goRoutineStopChan := make(chan int, goRoutineCnt)
	subStop := make(chan int, 1)
	//ctx := context.Background()

	log.Println("main start")

	shutdown := make(chan os.Signal, 1)
	signal.Notify(shutdown, os.Interrupt, syscall.SIGTERM)

	for i := 0; i < goRoutineCnt; i++ {
		wg.Add(1)
		go worker(i, &wg, subWorkerChan, goRoutineStopChan)
	}

	wg.Add(1)
	go addSub(&wg, subWorkerChan, subStop)

	select {
	case sig := <-shutdown:
		log.Println("main gets sig ", sig)
		//fallthrough
		//case <-ctx.Done():
		//log.Println("get ctx done.")
		subStop <- 1
		log.Printf("shuting down all %v goroutines.", goRoutineCnt)
		for i := 0; i < goRoutineCnt; i++ {
			goRoutineStopChan <- i
		}
	}

	wg.Wait()
	log.Println("after wg wait.")
	close(subWorkerChan)
	close(goRoutineStopChan)

	log.Println("Shutdown main.")
}

func addSub(wg *sync.WaitGroup, workerChan chan SubWorkerChan, stop chan int) {
	defer wg.Done()
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	failOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	ch, err := conn.Channel()
	failOnError(err, "Failed to open a channel")
	defer ch.Close()

	err = ch.ExchangeDeclare(
		"logs_direct", // name
		"direct",      // type
		true,          // durable
		false,         // auto-deleted
		false,         // internal
		false,         // no-wait
		nil,           // arguments
	)
	failOnError(err, "Failed to declare an exchange")

	q, err := ch.QueueDeclare(
		"",    // name
		false, // durable
		false, // delete when unused
		true,  // exclusive
		false, // no-wait
		nil,   // arguments
	)
	failOnError(err, "Failed to declare a queue")

	if len(os.Args) < 2 {
		log.Printf("Usage: %s [info] [warning] [error]", os.Args[0])
		os.Exit(0)
	}
	for _, s := range os.Args[1:] {
		log.Printf("Binding queue %s to exchange %s with routing key %s",
			q.Name, "logs_direct", s)
		err = ch.QueueBind(
			q.Name,        // queue name
			s,             // routing key
			"logs_direct", // exchange
			false,
			nil)
		failOnError(err, "Failed to bind a queue")
	}

	msgs, err := ch.Consume(
		q.Name, // queue
		"",     // consumer
		true,   // auto ack
		false,  // exclusive
		false,  // no local
		false,  // no wait
		nil,    // args
	)
	failOnError(err, "Failed to register a consumer")

	for {
		select {
		case d := <-msgs:
			workerChan <- SubWorkerChan{mqChan: ch, message: d.Body}
		case <-stop:
			log.Println("stopping sub func.")
			return
		}
	}
	log.Println("sub should not be here.")
}
