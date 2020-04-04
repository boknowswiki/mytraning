package main

import (
	"fmt"
)

func main() {
	favSpot := "comming"
	switch favSpot {
	case "not comming":
		fmt.Println("not comming\n")
	case "comming":
		fmt.Println("comming\n")
	}
}
