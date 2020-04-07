package main

import (
	"fmt"
	"sync"
)

func main() {
	c := make(chan int)
	var wg sync.WaitGroup
	go func() {
		for i := 0; i < 10; i++ {
			wg.Add(1)
			go func() {
				for i := 0; i < 10; i++ {
					c <- i
				}
				wg.Done()
			}()
		}

		wg.Wait()
		close(c)
	}()

	for v := range c {
		fmt.Println(v)
	}
}
