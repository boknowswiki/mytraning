package main

import (
	"fmt"
)

var x int
var y string
var z bool

func main() {
	x = 42
	y = "james bond"
	z = true

	s := fmt.Sprintf("%v, %v, %v", x, y, z)
	fmt.Println(x, y, z)
	fmt.Println(x)
	fmt.Println(y)
	fmt.Println(z)
	fmt.Println(s)
}
