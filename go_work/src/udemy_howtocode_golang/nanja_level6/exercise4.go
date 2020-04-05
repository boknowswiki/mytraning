package main

import (
	"fmt"
)

type person struct {
    first   string
    last    string
    age     int
}

func main() {
    p :=  person {
        first: "first",
        last:   "last",
        age:    2,
    }
    fmt.Println(p)

    p.speak()
}

func (p person) speak () {
    fmt.Println(p.first, p.last, p.age)
}

