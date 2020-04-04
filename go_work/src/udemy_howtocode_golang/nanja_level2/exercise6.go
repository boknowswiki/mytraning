package main

import (
	"fmt"
)

const (
	current_year             = 2020 + iota
	next_year                = current_year + iota
	next_next_year           = current_year + iota
	next_next_next_year      = current_year + iota
	next_next_next_next_year = current_year + iota
)

func main() {
	fmt.Println(current_year, next_year, next_next_year, next_next_next_year, next_next_next_next_year)

}
