package main

// hash
// time O(n), space O(n)
import (
	"fmt"
)

/**
 * @param secret: An string
 * @param guess: An string
 * @return: An string
 */
func getHint(secret string, guess string) string {
	// write your code here
	numberCount := make(map[uint8]int, 10)
	for i := 0; i < len(secret); i++ {
		numberCount[secret[i]]++
	}

	fmt.Println(numberCount)

	bull := 0
	cow := 0

	for i := 0; i < len(guess); i++ {
		if _, ok := numberCount[guess[i]]; !ok {
			continue
		}

		fmt.Println(numberCount, guess[i])

		if guess[i] == secret[i] {
			bull++
		} else if guess[i] != secret[i] && numberCount[guess[i]] > 0 {
			cow++
		}
		numberCount[guess[i]] = numberCount[guess[i]] - 1
	}

	ret := fmt.Sprintf("%dA%dB", bull, cow)
	return ret
}

func main() {
	//a := "1807"
	//b := "7810"
	a := "1123"
	b := "0111"
	fmt.Println(getHint(a, b))
}
