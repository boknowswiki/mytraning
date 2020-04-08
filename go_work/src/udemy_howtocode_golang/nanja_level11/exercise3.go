package main

import (
    "fmt"
)

type person struct {
    First   string
    Last    string
    Sayings []string
}

type customErr struct {
    say string
}

func (c customErr) Error () string {
        return c.say
}

func main() {

    c := customErr {
        say: "i am error",
    }

    foo(c)

}

func foo (e error) {
    fmt.Println(e)
}
