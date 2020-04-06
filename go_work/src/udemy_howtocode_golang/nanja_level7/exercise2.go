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
    p := person {
        first:  "first",
        last:   "last",
        age:    3,
    }

    fmt.Println(p)
    changeme(&p)
    fmt.Println(p)
}

func changeme(p *person) {
    fmt.Println((*p).first, (*p).last, (*p).age)

    (*p).first = "second"
    (*p).age = 4
}

