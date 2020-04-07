package main

import (
    "sync"
    "sync/atomic"
	"fmt"
    "runtime"
)

type person struct {
    first string
}

func (p person) speak () {
    fmt.Println(p.first)
}


func main() {
    p := person {
        first: "first",
    }
    var wg sync.WaitGroup
    fmt.Println(runtime.GOARCH)
    //fmt.Println(runtime.NumCPU())
    //fmt.Println(runtime.NumGoroutine())
    var cnt int64

    for i:= 0; i < 100; i++ {
        wg.Add(1)
        go func () {
            atomic.AddInt64(&cnt, 1)
            //fmt.Println(y)
            wg.Done()
        }()
    }

    //fmt.Println(runtime.NumGoroutine())
    wg.Wait()

    fmt.Println(cnt)
    fmt.Println(p)
    p.speak()
}
