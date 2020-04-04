package main

import (
    "fmt"
    "time"
)

func case1( ch chan string) {
    ch <- "from case1"
}

func main() {
    ch := make(chan string)
    var cnt int

    go case1(ch)

    for {
        time.Sleep(1*time.Second)
        cnt += 1
        select {
            case s := <-ch:
                fmt.Println(s, cnt)
            default:
                fmt.Println("default here", cnt)
        }
    }
}
