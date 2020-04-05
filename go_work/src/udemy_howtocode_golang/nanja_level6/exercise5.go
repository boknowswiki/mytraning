package main

import (
	"fmt"
)

type square struct {
    s     int
}

type circle struct {
    r     int
}

type shape interface {
    area() int
}

func main() {
    s := square {
        s: 3,
    }

    c := circle {
        r: 4,
    }

    fmt.Println(s)
    fmt.Println(c)

    info(s)
    info(c)
}

func info (sh shape) {
    fmt.Println(sh.area())
}

func (s square) area () (int) {
    return s.s*s.s
}

func (c circle) area () (int) {
    return 3*c.r*c.r
}

