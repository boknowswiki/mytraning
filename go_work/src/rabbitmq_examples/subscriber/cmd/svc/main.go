package main

import (
	"log"
	"os"

	"github.com/boknowswiki/mytraning/go_work/src/rabbitmq_examples/subscriber/internal/mq"
	"github.com/streadway/amqp"
	cli "github.com/urfave/cli/v2"
)

func failOnError(err error, msg string) {
	if err != nil {
		log.Fatalf("%s: %s", msg, err)
	}
}

func main() {
	app := &cli.App{
		Flags: []cli.Flag{
			&cli.StringFlag{
				Name: "exchange",
				//Value:       "english",
				Aliases: []string{"e"},
				Usage:   "send message to this exchange",
			},
			&cli.StringFlag{
				Name:    "service",
				Aliases: []string{"s"},
				Usage:   "service name",
			},
		},
		Action: func(c *cli.Context) error {
			topicHandler(c)
			return nil
		},
	}

	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}

func topicHandler(c *cli.Context) error {
	ex := c.String("exchange")
	log.Printf("get operation %v", ex)
	s := c.String("service")
	log.Printf("get service %v", s)

	conn, _ := mq.NewConn()
	defer conn.Close()
	ch, _ := mq.NewChannel(conn)
	defer ch.Close()

	err := ch.ExchangeDeclare(
		ex,       // name
		"direct", // type
		true,     // durable
		false,    // auto-deleted
		false,    // internal
		false,    // no-wait
		nil,      // arguments
	)
	failOnError(err, "Failed to declare an exchange")

	body := mq.BuildMessage("add", s)
	err = ch.Publish(
		ex,    // exchange
		s,     // routing key
		false, // mandatory
		false, // immediate
		amqp.Publishing{
			ContentType: "text/plain",
			Body:        body,
		})
	failOnError(err, "Failed to publish a message")

	log.Printf(" [x] Sent %s", body)

	return nil
}
