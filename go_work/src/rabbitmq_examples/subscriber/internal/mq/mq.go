package mq

import (
	"log"

	"encoding/json"

	"github.com/streadway/amqp"
)

// EventBusTopicType has the eventbus topic type for adding or deleting subscription.
type EventBusTopicType int

const (
	// EventBusTopicAdd adds subscription type.
	EventBusTopicAdd EventBusTopicType = iota
	// EventBusTopicUpdate updates subscription type.
	EventBusTopicUpdate
	// EventBusTopicDelete deletes subscription type.
	EventBusTopicDelete
)

// EventBusSubMessage defines service name needs to be subscribed.
type EventBusSubMessage struct {
	ServiceName string
}

// EventBusTopicMessage defines the message format.
type EventBusTopicMessage struct {
	EventBusTopicType EventBusTopicType
	Message           string
}

// NewConn gets new connection to rabbitmq.
func NewConn() (*amqp.Connection, error) {
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	if err != nil {
		log.Panicln("init rabbitmq conn error: ", err)
	}

	return conn, nil
}

// NewChannel gets new channel from the connection to rabbitmq.
func NewChannel(conn *amqp.Connection) (*amqp.Channel, error) {
	ch, err := conn.Channel()
	if err != nil {
		log.Panic("failed to open a channel error: ", err)
		conn.Close()
	}

	return ch, nil
}

// BuildMessage build a topic message for sub.
func BuildMessage(op string, rk string) []byte {
	topicType := EventBusTopicAdd
	switch op {
	case "add":
		topicType = EventBusTopicAdd
	case "update":
		topicType = EventBusTopicUpdate
	case "delete":
		topicType = EventBusTopicDelete
	default:
		log.Fatalf("unsupported topic type %v", op)
	}
	msg := EventBusTopicMessage{
		EventBusTopicType: topicType,
		Message:           rk,
	}

	s, _ := json.Marshal(msg)

	return s
}

// GetMessage revert the topic message for sub.
func GetMessage(b []byte) EventBusTopicMessage {
	var msg EventBusTopicMessage

	json.Unmarshal(b, &msg)

	return msg
}

func listenToTopic(conn *amqp.Connection) {

}
