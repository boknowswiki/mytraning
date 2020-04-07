package main

import (
    "sync"
	"fmt"
    "runtime"
)


func main() {
    var wg sync.WaitGroup
    //fmt.Println(runtime.NumCPU())
    //fmt.Println(runtime.NumGoroutine())
    var cnt int

    for i:= 0; i < 100; i++ {
        wg.Add(1)
        go func () {
            y := cnt
            runtime.Gosched()
            y++
            cnt = y
            //fmt.Println(y)
            wg.Done()
        }()
    }

    //fmt.Println(runtime.NumGoroutine())
    wg.Wait()

    fmt.Println(cnt)
}
