package main

import (
	"fmt"
)


func main() {
    f := foo()
    bi, bs := bar()

    fmt.Println(f)
    fmt.Println(bi, bs)
}

func foo () int {
    return 1
}

func bar () (int, string) {
    return 2, "hello"
}
