package main

import (
	"fmt"
)

type person struct {
    first string
}

func (p *person) speak () {
    fmt.Println(p.first)
}

type human interface {
    speak()
}

func saySomething (h human) {
    h.speak()
}

func main() {
    p := person {
        first: "first",
    }

    saySomething(&p)
}
