/**
 * @param s: an expression includes numbers, letters and brackets
 * @return: a string
 */

import (
    "unicode"
)

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
