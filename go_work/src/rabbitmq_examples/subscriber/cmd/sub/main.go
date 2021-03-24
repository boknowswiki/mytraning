package main

import (
	"log"
	"os"
	"os/signal"
	"strings"
	"sync"
	"syscall"

	"github.com/boknowswiki/mytraning/go_work/src/rabbitmq_examples/subscriber/internal/mq"
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
		// get our eventbus customized struct with callback url and eventbusMsg struct {body: from rmq/kafka, connectorType: "rmq/kafka"}
		case msg := <-subWorkerChan:
			log.Printf("worker %v gets message %v", id, string(msg.message))
			// send to callback url 1 success: nack, 2 failed(retries): ack.
			// eventbusMsg {
			// body message rmq/kafka
			// connector type
			// }
		case <-stop:
			log.Printf("stoping worker %v.", id)
			return
		}
	}

	//log.Println("worker should not be here.")
}

func main() {
	var wg sync.WaitGroup
	goRoutineCnt := DEFAULTGOROUTINECNT
	// dispatch the service message from the service queues.
	subWorkerChan := make(chan SubWorkerChan, goRoutineCnt)
	//finish := make(chan struct{})
	// declaring finish to be of type chan struct{} says that the channel contains no value; we’re only interested in its closed property.
	goRoutineStopChan := make(chan int)
	subStop := make(chan int)
	subTopicStop := make(chan int)
	//ctx := context.Background()

	log.Println("main start")

	conn, _ := mq.NewConn()
	defer conn.Close()
	// one channel per go routine.
	// check best practice for creating channel/connection to rabbitmq.
	// ans: use one connection and separate channels for different go-routine.
	ch, _ := mq.NewChannel(conn)
	defer ch.Close()

	shutdown := make(chan os.Signal, 1)
	signal.Notify(shutdown, os.Interrupt, syscall.SIGTERM)

	for i := 0; i < goRoutineCnt; i++ {
		wg.Add(1)
		go worker(i, &wg, subWorkerChan, goRoutineStopChan)
	}

	wg.Add(1)
	go listenToTopic(&wg, ch, subTopicStop, subWorkerChan, subStop)

	select {
	case sig := <-shutdown:
		log.Println("main gets sig ", sig)
		//fallthrough
		//case <-ctx.Done():
		//log.Println("get ctx done.")
		close(subTopicStop)
		// maybe need to stop all the subscriber go routine before close this channel.
		// need to think a logic to do this close channel right.
		// doesn't nee to do it that way.
		close(subWorkerChan)
		close(subStop)
		log.Printf("shuting down all %v goroutines.", goRoutineCnt)
		close(goRoutineStopChan)
	}

	wg.Wait()
	//log.Println("after wg wait.")

	log.Println("Shutdown main.")
}

func listenToTopic(wg *sync.WaitGroup, ch *amqp.Channel, stop chan int, subWorkerChan chan SubWorkerChan, subStop chan int) {
	defer wg.Done()

	err := ch.ExchangeDeclare(
		"sub_topic", // name
		"topic",     // type
		true,        // durable
		false,       // auto-deleted
		false,       // internal
		false,       // no-wait
		nil,         // arguments
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

	s := "service"
	log.Printf("Binding queue %s to exchange %s with routing key %s",
		q.Name, "sub_topic", s)
	err = ch.QueueBind(
		q.Name,      // queue name
		s,           // routing key
		"sub_topic", // exchange
		false,
		nil)
	failOnError(err, "Failed to bind a queue")

	msgs, err := ch.Consume(
		q.Name, // queue
		"",     // consumer
		true,   // auto ack
		false,  // exclusive
		false,  // no local
		false,  // no wait
		nil,    // args
	)

	subToChan := make(map[string]chan int)

	for {
		select {
		case d := <-msgs:
			//log.Printf(" [x] %s", d.Body)
			msg := mq.GetMessage(d.Body)
			log.Printf("get topic msg %#v", msg)
			subMsg := mq.EventBusSubMessage{ServiceName: msg.Message}
			qName := "serviceQueue"
			log.Printf("get qname %v", qName)
			switch t := msg.EventBusTopicType; t {
			case mq.EventBusTopicAdd:
				deleteChan := make(chan int)
				//log.Printf("deleteChan addr %v", &deleteChan)
				subToChan[qName] = deleteChan
				go addSub(wg, ch, qName, subMsg, subWorkerChan, subStop, deleteChan)
			case mq.EventBusTopicUpdate:
				log.Println("need to update service go routine queue binding.")
				newS := strings.Split(subMsg.ServiceName, ",")
				log.Printf("get old binding key %v, new binding key %v", newS[0], newS[1])
				err = ch.QueueUnbind(
					qName,         //queue name
					newS[0],       // binding key
					"sub_service", //exchange
					nil)
				err = ch.QueueBind(
					qName,         // queue name
					newS[1],       // binding key
					"sub_service", // exchange
					false,
					nil)
				log.Println("finish unbind and bind.")
			case mq.EventBusTopicDelete:
				log.Println("need to delete service go routine.")
				del := subToChan[qName]
				//log.Printf("del addr %v", del)
				close(del)
				log.Printf("%v should be deleted.", qName)
			}
		case <-stop:
			log.Println("stopping listenToTopic goroutine.")
			return
		}
	}
}

func addSub(wg *sync.WaitGroup, ch *amqp.Channel, qName string, msg mq.EventBusSubMessage, workerChan chan SubWorkerChan, stop chan int, del chan int) {
	wg.Add(1)
	defer wg.Done()

	//log.Printf("sub get del addr %v", del)
	err := ch.ExchangeDeclare(
		"sub_service", // name
		"direct",      // type
		true,          // durable
		false,         // auto-deleted
		false,         // internal
		false,         // no-wait
		nil,           // arguments
	)
	failOnError(err, "Failed to declare an exchange")

	q, err := ch.QueueDeclare(
		qName, // name
		false, // durable
		false, // delete when unused
		true,  // exclusive
		false, // no-wait
		nil,   // arguments
	)
	failOnError(err, "Failed to declare a queue")

	err = ch.QueueBind(
		q.Name,
		msg.ServiceName,
		"sub_service",
		false,
		nil,
	)
	failOnError(err, "Failed to bind a queue")

	log.Printf("bind to exchange sub_service binding key %v on %v.", msg.ServiceName, q.Name)
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
		// get the message from rmq service queue.
		case d := <-msgs:
			// build callback url
			// form a message struct {body: d, connectorType: "rmq/kafka",....}
			workerChan <- SubWorkerChan{mqChan: ch, message: d.Body}

		case <-stop:
			log.Println("stopping sub func.")
			return
		case <-(del):
			log.Println("got delete sub signal.")
			return
		}
	}
	//log.Println("sub should not be here.")
}
