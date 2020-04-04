package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"net"
)

const (
	serverIP   = "127.0.0.1"
	serverPort = "28880"
	connType   = "tcp"
)

// Client for golang library
type Client struct {
	MesgIn   []byte
	MesgOut  []byte
	Conn     net.Conn
	NotiConn net.Conn
	Notify   chan int
	Conneted bool
}

type GoObj struct {
	Target   string
	Req_type string
	Tx_id    string
	Node     string
	Data     string
	Status   int
}

type resp struct {
	Data   string
	Status int
	Tx_id  string
	Target string
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

func newClient() *Client {
	var client Client
	fmt.Println(client.Conn)
	conn, err := net.Dial(connType, serverIP+":"+serverPort)
	checkError(err)
	client.Conn = conn

	//conn, err = net.Dial(connType, serverIP+":"+serverPort)
	//checkError(err)
	//client.NotiConn = conn
	client.Conneted = true

	go (&client).notiRecv()
	//need to wait the noticonn back

	return &client
}

func (client *Client) fetch(obj GoObj) resp {
	var res resp
	out, err := json.Marshal(obj)
	checkError(err)
	out = append(out, "\n"...)
	fmt.Println(out)
	client.sendToServer(out)
	client.recvFromServer(&res)

	return res
}

func (client *Client) modify() {
	fmt.Println("this is modify")
}

func (client *Client) sendToServer(out []byte) {
	client.Conn.Write(out)
}

func (client *Client) recvFromServer(res *resp) {
	r := bufio.NewReader(client.Conn)
	fmt.Println("waiting for read")
	deli := '\n'
	line, err := r.ReadBytes(byte(deli))

	checkError(err)

	fmt.Println("got ", line)
	fmt.Println(string(line))

	json.Unmarshal(line, res)
}

func (client *Client) notiRecv() {
start:
	conn, err := net.Dial(connType, serverIP+":"+serverPort)
	checkError(err)
	client.NotiConn = conn
	defer client.NotiConn.Close()

	notiRead := make(chan error)
	r := bufio.NewReader(client.NotiConn)
	deli := '\n'

	go func() {
		for {
			line, err := r.ReadBytes(byte(deli))
			if err != nil {
				notiRead <- err
				if io.EOF == err {
					fmt.Println("server side closed")
					close(notiRead)
					client.NotiConn.Close()
					return
				}
				fmt.Println(line)
			}
			//get call back function and run with go cb_func

		}
	}()

	for {
		select {
		case err := <-notiRead:
			fmt.Println("connection dropped: ", err)
			if err == io.EOF {
				goto start
			}
		}
	}
}
