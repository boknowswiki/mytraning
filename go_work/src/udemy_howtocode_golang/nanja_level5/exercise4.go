package main

import (
	"fmt"
)

func main() {

    p1 := struct {
            first string
            keys    []string
        } {
            first: "1",
            keys: []string {"a", "b", "abc"},
    }


    fmt.Println(p1)
    fmt.Println(p1.keys[0])
}
