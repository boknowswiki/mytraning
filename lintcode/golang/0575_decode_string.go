/**
 * @param s: an expression includes numbers, letters and brackets
 * @return: a string
 */

import (
    "unicode"
)

// stack
// time O(n)

func expressionExpand(s string) string {
    var stack []rune
	for _, ch := range s {
		if ch != ']' {
			stack = append(stack, ch)
			continue
		}

		var strings []rune
		for len(stack) > 0 && stack[len(stack)-1] != '[' {
			strings = append(strings, stack[len(stack)-1])
			stack = stack[:len(stack)-1]
		}

		// jump over '['
		stack = stack[:len(stack)-1]

		num := 0
		base := 1
		for len(stack) > 0 && unicode.IsNumber(stack[len(stack)-1]) {
			num += int((stack[len(stack)-1] - '0')) * base
			base *= 10
			stack = stack[:len(stack)-1]
		}

		for i := 0; i < num; i++ {
			for iStr := len(strings) - 1; iStr >= 0; iStr-- {
				stack = append(stack, strings[iStr])
			}
		}
	}
	return string(stack)
}


package main

// stack and dfs

import (
	"fmt"
	"unicode"
)

/**
 * @param s: an expression includes numbers, letters and brackets
 * @return: a string
 */
func expressionExpand(s string) string {
	// write your code here
	n := len(s)
	if n == 0 {
		return ""
	}

	ret, _ := dfs(s, 0)

	return ret
}

func dfs(s string, index int) (string, int) {
	var ret string
	var reps int

	fmt.Println("enter dfs with index: ", index)
	for index < len(s) {
		var subString string
		if unicode.IsNumber(rune(s[index])) {
			reps = reps*10 + int(s[index]-'0')
		} else if s[index] == '[' {
			subString, index = dfs(s, index+1)
			fmt.Println("get substring ", subString, "index: ", index)
			for i := 0; i < reps; i++ {
				ret += subString
			}
			reps = 0
		} else if s[index] == ']' {
			fmt.Println("return ret ", ret, "index: ", index)
			return ret, index
		} else {
			ret += string(s[index])
		}
		index++
	}
	return ret, index
}

func main() {
	a := "abc3[a]"
	fmt.Println(expressionExpand(a))
}

