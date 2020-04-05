package main

import (
	"fmt"
)

type person struct {
    first   string
    last    string
    flavors []string
}

func main() {
    p1 := person {
        first:  "p",
        last:   "1",
        flavors: []string {"a", "b", "abc"},
    }

    p2 := person {
        first:  "p",
        last:   "2",
        flavors: []string {"e", "f", "efg"},
    }

    fmt.Println(p1.first, p1.last, p1.flavors)
    fmt.Println(p2.first, p2.last, p2.flavors)

    for i, v := range p1.flavors {
        fmt.Println(i, v)
    }

    for i, v := range p2.flavors {
        fmt.Println(i, v)
    }

    fmt.Printf("%T\n", p1)
}
