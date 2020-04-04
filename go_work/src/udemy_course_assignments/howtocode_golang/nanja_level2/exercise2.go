package main

import (
	"fmt"
)

func main() {
	a := (1 == 1)
	b := (1 <= 1)
	c := (1 >= 1)
	d := (1 != 1)
	e := (1 < 1)
	f := (1 > 1)

	fmt.Printf("%t\n", a)
	fmt.Printf("%t\n", b)
	fmt.Printf("%t\n", c)
	fmt.Printf("%t\n", d)
	fmt.Printf("%t\n", e)
	fmt.Printf("%t\n", f)

}
