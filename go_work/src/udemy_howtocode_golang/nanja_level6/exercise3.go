package main

import (
	"fmt"
)


func main() {
    a := []int {1, 2, 3, 4, 5, 6, 7 ,8, 9, 10,}
    b := []int {1, 2, 3, 4,}
    c := []int {5, 6, 7, 8,}
    d := []int {9, 10,}
    defer foo(a...)
    bb := bar(b, c, d)

    fmt.Println(bb)
}

func foo (x ...int) int {
    total := 0
    for _, v := range x {
        total += v
    }

    fmt.Println("total is", total)
    return total
}

func bar (x ...[]int) int {
    total := 0

    for _, v := range x {
        for _, vv := range v {
            total += vv
        }
    }

    return total
}
