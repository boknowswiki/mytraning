package main

import (
	"fmt"
)

func main() {
    x := 0

    func () {
        x++
    }()

    fmt.Println(x)
}


