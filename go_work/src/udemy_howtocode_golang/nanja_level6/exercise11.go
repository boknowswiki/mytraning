package main

import (
	"fmt"
)

func main() {
    x := 5
    fmt.Println(f(x))
}

func f (x int) int {
    if x == 1 {
        return 1
    }

    return x * f(x-1)
}


