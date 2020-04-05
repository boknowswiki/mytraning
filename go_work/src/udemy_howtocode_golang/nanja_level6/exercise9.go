package main

import (
	"fmt"
)

func main() {
    x := func() {
        fmt.Println("this is foo")
    }

    foo(x)

}

func foo (f func()){
    f()
}


