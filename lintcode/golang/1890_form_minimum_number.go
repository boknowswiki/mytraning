package main

import (
	"fmt"
)

/**
 * @param str: the pattern
 * @return: the minimum number
 */
func formMinimumNumber(str string) string {
	// Write your code here.

	n := len(str)
	ret := make([]uint8, n+1)
	cnt := 1

	for i := 0; i < n+1; i++ {
		if i == n || string(str[i]) == "I" {
			for j := i - 1; j > -2; j-- {
				ret[j+1] = uint8(int('0') + cnt)
				//fmt.Println(ret)
				cnt++
				if j >= 0 && string(str[j]) == "I" {
					break
				}
			}
		}
	}
	//fmt.Println(ret)

	return string(ret)
}

func main() {
	a := "DIDI"

	fmt.Println(formMinimumNumber(a))
}
