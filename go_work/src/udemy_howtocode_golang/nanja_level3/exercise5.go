package main

import (
	"fmt"
)

func main() {
	for i := 10; i <= 100; i++ {
		fmt.Printf("number %d divided by 4, reminder %d\n", i, i%4)

	}
}
