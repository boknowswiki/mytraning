package main

import (
	"fmt"
)

func main() {
    x := []string {"James", "Bond", "Shaken, not stirred"}
    y := []string {"Miss", "Moneypenny", "Helloooooo, James."}
    z := [][]string {x, y}

    fmt.Println(z)

    for i, v := range z {
        fmt.Println(i, v)
        for j, vv := range v {
            fmt.Println(j, vv)
        }
    }
}
