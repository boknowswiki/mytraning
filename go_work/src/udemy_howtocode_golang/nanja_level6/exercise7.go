package main

import (
	"fmt"
)

func main() {
    x := foo

    x()
}

func foo () {
    fmt.Println("this is foo")
}


