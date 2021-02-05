package main

import (
	"encoding/json"
	"log"
	"os"

	"github.com/streadway/amqp"
)

// EventBusTopicType has the eventbus topic type for adding or deleting subscription.
type EventBusTopicType int

const (
	// EventBusTopicAdd adds subscription type.
	EventBusTopicAdd EventBusTopicType = iota
	// EventBusTopicDelete deletes subscription type.
	EventBusTopicDelete
)

// EventBusTopicMessage defines the message format.
type EventBusTopicMessage struct {
	EventBusTopicType EventBusTopicType
	Message           string
}

func failOnError(err error, msg string) {
	if err != nil {
		log.Fatalf("%s: %s", msg, err)
	}
}

func main() {
	if len(os.Args) < 2 {
		log.Println("need a binding key for this topic")
		return
	}

	run()
}

func run() {
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	failOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	ch, err := conn.Channel()
	failOnError(err, "Failed to open a channel")
	defer ch.Close()

	err = ch.ExchangeDeclare(
		"logs_topic", // name
		"topic",      // type
		true,         // durable
		false,        // auto-deleted
		false,        // internal
		false,        // no-wait
		nil,          // arguments
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
		log.Printf("Usage: %s [binding_key]...", os.Args[0])
		os.Exit(0)
	}
	for _, s := range os.Args[1:] {
		log.Printf("Binding queue %s to exchange %s with routing key %s",
			q.Name, "logs_topic", s)
		err = ch.QueueBind(
			q.Name,       // queue name
			s,            // routing key
			"logs_topic", // exchange
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

	forever := make(chan bool)

	go func() {
		for d := range msgs {
			log.Printf(" [x] %s", d.Body)
			msg := getMessage(d.Body)
			log.Printf("msg %#v", msg)
		}
	}()

	log.Printf(" [*] Waiting for logs. To exit press CTRL+C")
	<-forever
}

func getMessage(b []byte) EventBusTopicMessage {
	var msg EventBusTopicMessage

	json.Unmarshal(b, &msg)

	return msg
}
