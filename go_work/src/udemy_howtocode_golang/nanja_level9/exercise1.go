package main

import (
    "sync"
	"fmt"
    "runtime"
)


func main() {
    var wg sync.WaitGroup
    fmt.Println(runtime.NumCPU())
    fmt.Println(runtime.NumGoroutine())

    for i:= 0; i < 2; i++ {
        wg.Add(1)
        go func (y int) {
            fmt.Println(y)
            wg.Done()
        }(i)
    }

    fmt.Println(runtime.NumGoroutine())
    wg.Wait()
}
