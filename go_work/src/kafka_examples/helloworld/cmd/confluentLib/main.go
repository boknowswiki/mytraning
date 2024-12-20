package main

import (
	"context"
	"fmt"
	"strconv"
	"time"

	"github.com/confluentinc/confluent-kafka-go/kafka"
)

var topic string

func produce(ctx context.Context) {
	// initialize a counter
	i := 0
	topic = "helloworld"

	p, err := kafka.NewProducer(&kafka.ConfigMap{
		"bootstrap.servers": "localhost",
		"acks":              "all"})

	if err != nil {
		fmt.Printf("Failed to create producer: %s\n", err)
		return
	}

	defer p.Close()

	for {
		select {
		case <-ctx.Done():
			return
		default:
			p.Produce(&kafka.Message{
				TopicPartition: kafka.TopicPartition{Topic: &topic, Partition: kafka.PartitionAny},
				Key:            []byte(strconv.Itoa(i)),
				Value:          []byte("this is message" + strconv.Itoa(i)),
			}, nil)
			// each kafka message has a key and value. The key is used
			// to decide which partition (and consequently, which broker)
			// the message gets published on

			// log a confirmation once the message is written
			fmt.Println("writes:", i)
			i++
			// sleep for a second
			time.Sleep(time.Second)
		}
	}
}

func consume(ctx context.Context) {
	// initialize a new reader with the brokers and topic
	// the groupID identifies the consumer and prevents
	// it from receiving duplicate messages
	cm := kafka.ConfigMap{
		"bootstrap.servers":  "localhost",
		"group.id":           "myGroup",
		"auto.offset.reset":  "earliest",
		"enable.auto.commit": false,
	}
	c, err := kafka.NewConsumer(&cm)

	if err != nil {
		panic(err)
	}

	//fmt.Printf("configmap is %#v\n", cm)
	//fmt.Println("auto commit enable: ", cm.Get("auto.commit.enable"))

	c.Subscribe(topic, nil)
	defer c.Close()

	for {
		select {
		case <-ctx.Done():
			return
		default:
			msg, err := c.ReadMessage(-1)
			if err == nil {
				fmt.Printf("Message on %s: %s\n", msg.TopicPartition, string(msg.Value))
				offset, err := c.Commit()
				if err != nil {
					fmt.Printf("commit error %v\n", err)
				} else {
					fmt.Printf("commit to offset %v\n", offset)
				}
			} else {
				// The client will automatically try to recover from all errors.
				fmt.Printf("Consumer error: %v (%v)\n", err, msg)
			}

		}
	}
}

// need to run ./bin/kafka-topics.sh --create --topic helloworld --bootstrap-server localhost:9092.
func main() {
	// create a new context
	ctx := context.Background()
	// produce messages in a new go routine, since
	// both the produce and consume functions are
	// blocking
	go produce(ctx)
	consume(ctx)
}
