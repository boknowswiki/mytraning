package main

import (
	"fmt"
)

func main() {
    x := func() {
        fmt.Println("this is foo")
    }

    {
        y := 1
        fmt.Println(y)
    }

    x()
}


