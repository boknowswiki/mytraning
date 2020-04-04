package main

import (
	"fmt"
	"io/ioutil"

	"github.com/golang/protobuf/proto"
)

const (
	TESTFILE = "protobuf_test"
)

func main() {
	p := Person{
		Id:    1234,
		Name:  "test",
		Email: "test@test.com",
		Phones: []*Person_PhoneNumber{
			{Number: "123456", Type: Person_HOME},
		},
	}

	var people []*Person
	people = append(people, &p)

	book := &AddressBook{
		People: people,
	}

	out, err := proto.Marshal(book)
	if err != nil {
		fmt.Println("encode err:", err)
	}

	fmt.Println("out is ", out)

	err = ioutil.WriteFile(TESTFILE, out, 0644)
	if err != nil {
		fmt.Println("write file ", TESTFILE, "error: ", err)
	}

	in, err := ioutil.ReadFile(TESTFILE)
	if err != nil {
		fmt.Println("read file ", TESTFILE, "error: ", err)
	}

	newbook := &AddressBook{}
	if err := proto.Unmarshal(in, newbook); err != nil {
		fmt.Println("decode failed ", err)
	}

	fmt.Println(in)
	fmt.Println(newbook)
}
