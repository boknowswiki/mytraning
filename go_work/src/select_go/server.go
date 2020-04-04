package main

import (
	"fmt"
	"io"
	"net"
	"os"
)

const (
	CONN_HOST = "localhost"
	CONN_PORT = "9999"
	CONN_TYPE = "tcp"
)

func main() {
	fmt.Println("Hi me! Starting the server ...")

	// Listen for incoming connections
	lis, err := net.Listen(CONN_TYPE, CONN_HOST+":"+CONN_PORT)
	if err != nil {
		fmt.Printf("Error to listening on %s:%s with error %s", CONN_HOST, CONN_PORT, err.Error)
		os.Exit(1)
	}

	defer lis.Close()
	fmt.Println("Listening on", CONN_HOST+":"+CONN_PORT)
	for {
		conn, err := lis.Accept()
		if err != nil {
			fmt.Println("Accept error", err.Error())
			os.Exit(1)
		}

		go handlerRequest(conn)
	}
}

func handlerRequest(conn net.Conn) {
	buf := make([]byte, 1024)

	for {
		rLen, err := conn.Read(buf)
		if err != nil {
			if err == io.EOF {
				fmt.Println("Connection closed by client", err.Error())
				conn.Close()
				return
			}
			fmt.Println("Reading err:", err.Error)
		}

		fmt.Println("Got len ", rLen, "data: ", string(buf))
		//conn.Write(buf)
		//conn.Close()
	}
}
