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
    var mu sync.Mutex

    for i:= 0; i < 100; i++ {
        wg.Add(1)
        go func () {
            mu.Lock()
            y := cnt
            runtime.Gosched()
            y++
            cnt = y
            //fmt.Println(y)
            mu.Unlock()
            wg.Done()
        }()
    }

    //fmt.Println(runtime.NumGoroutine())
    wg.Wait()

    fmt.Println(cnt)
}
