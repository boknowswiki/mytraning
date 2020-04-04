package libclient

import (
	"fmt"
	"io"
	"net"
)

const (
	CONN_HOST = "localhost"
	CONN_PORT = "9999"
	CONN_TYPE = "tcp"
)

type connstate int

const (
	DESTRUCTING connstate = iota // start from 0
	DISCON
	CONPEND
	CONREQ
	CONNECT
	PUBLISHED
	ACTIVE
	DISABLED
)

type sysdclient struct {
	cstate connstate
	conn   *net.Conn
}

func createAndConnect() (*sysdclient, error) {
	var client sysdclient

	client.getconn()

	noti := make(chan error)

	go receivemsg(&client, noti)

	return &client, err
}

func (client sysdclient) getconn() error {
	conn, err := net.Dial(CONN_TYPE, CONN_HOST+":"+CONN_PORT)
	if err != nil {
		fmt.Println("Connecting to server error ", err.Error())
		return err
	}

	if client.conn != nil {
		(*client.conn).Close()
	}

	client.conn = &conn

	return err
}

func receivemsg(client *sysdclient, noti chan error) {
	buf := make([]byte, 1024)
	for {
		n, err := (*client.conn).Read(buf)
		if err != nil {
			noti <- err
			if err == io.EOF {
				fmt.Println("server side closed")
				close(noti)
				(*client.conn).Close()
				return
			}
		}
		if n > 0 {
			fmt.Println("got", buf[:n])
		}
	}
}
