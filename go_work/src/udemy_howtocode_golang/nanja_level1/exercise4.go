package main

import (
	"fmt"
)

type mine int

func main() {
	var x mine

	fmt.Println(x)
	fmt.Printf("type %T\n", x)

	x = 42
	fmt.Println(x)

}
