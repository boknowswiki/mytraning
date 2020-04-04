package main

import (
	"fmt"
	"io"
	"net"
	//"bufio"
)

const (
	CONN_HOST = "localhost"
	CONN_PORT = "9999"
	CONN_TYPE = "tcp"
)

func main() {

start:
	fmt.Println("Connecting to server...")

	conn, err := net.Dial(CONN_TYPE, CONN_HOST+":"+CONN_PORT)
	if err != nil {
		fmt.Println("Connecting to server error ", err.Error())
		goto start
		//os.Exit(1)
	}
	defer conn.Close()

	/*
		err = conn.(*net.TCPConn).SetKeepAlive(true)
		if err != nil {
			fmt.Println(err)
			return
		}

		err = conn.(*net.TCPConn).SetKeepAlivePeriod(30 * time.Second)
		if err != nil {
			fmt.Println(err)
			return
		}
	*/
	notify := make(chan error)

	go func() {
		buf := make([]byte, 1024)
		for {
			n, err := conn.Read(buf)
			if err != nil {
				notify <- err
				if io.EOF == err {
					fmt.Println("server side closed")
					close(notify)
					conn.Close()
					return
				}
			}
			if n > 0 {
				fmt.Println("unexpected data: %s", buf[:n])
			}
		}
	}()

	for {
		select {
		case err := <-notify:
			fmt.Println("connection dropped message", err)
			if err == io.EOF {
				fmt.Println("connection to server was closed")
				goto start
				//return
			}
			//break
		//case <-time.After(time.Second * 1):
		//	fmt.Println("timeout 1, still alive")
		default:
			fmt.Println("alive")
		}
	}
}
