package main

import (
    "sync"
    "sync/atomic"
	"fmt"
    "runtime"
)


func main() {
    var wg sync.WaitGroup
    fmt.Println(runtime.GOARCH)
    fmt.Println(runtime.GOOS)
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
}
