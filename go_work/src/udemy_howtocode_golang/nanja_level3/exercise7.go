package main

import (
	"fmt"
)

func main() {
	age := 0
	if age > 0 {
		fmt.Println("born\n")
	} else if age == 0 {
		fmt.Println("coming\n")
	} else {
		fmt.Println("not yet\n")
	}
}
