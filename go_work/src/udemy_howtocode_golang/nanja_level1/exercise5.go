package main

import (
	"fmt"
)

type mine int

func main() {
	var x mine
	var y int

	fmt.Println(x)
	fmt.Printf("type %T\n", x)

	x = 42
	fmt.Println(x)

	y = int(x)

	fmt.Println(y)
	fmt.Printf("type %T\n", y)

}
