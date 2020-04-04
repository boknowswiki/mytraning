package main

import (
    "fmt"
    "sync"
    //"time"
)

type counter struct {
    cnt int
    mux sync.Mutex
    wg sync.WaitGroup
}


var done chan bool

func main () {
    done = make(chan bool, 200)
    var c counter
    c.cnt = 0

    for i:= 0; i < 200; i++ {
        c.wg.Add(1)
        go add_one(&c)
    }

    //time.Sleep(time.Second)

    //for i:= 0; i < 200; i++ {
    //    <-done
    //}
    c.wg.Wait()

    fmt.Println("Final cnt is", c.cnt)

}

func add_one(ctner *counter) {
    defer ctner.wg.Done()
    ctner.mux.Lock()
    ctner.cnt += 1
    ctner.mux.Unlock()
    done <- true
}
