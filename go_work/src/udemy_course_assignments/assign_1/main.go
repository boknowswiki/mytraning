package main

import (
    "fmt"
)

func main() {
    var s [11]int

    for i, _ := range s {
        s[i] = i
        if s[i] % 2 == 0 {
            fmt.Println(s[i], " is even")
        } else {
            fmt.Println(s[i], " is odd")
        }
    }
}
