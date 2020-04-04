package main

import (
	"fmt"
)

type englishbot struct{}
type spinashbot struct{}

type bot interface {
	getGreeting() string
	//getword() string
}

func main() {
	eb := englishbot{}
	sb := spinashbot{}

	printGreeting(eb)
	//getword(eb)
	printGreeting(sb)

}

func printGreeting(b bot) {
	fmt.Println(b.getGreeting())
}

func (englishbot) getGreeting() string {
	return "hello"
}

func (englishbot) getword() string {
	return "word"
}

func (spinashbot) getGreeting() string {
	return "hola"
}

//func (spinashbot) getword() string {
//	return "s word"
//}
