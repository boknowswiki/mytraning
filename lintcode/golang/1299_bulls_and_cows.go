//hash

/**
 * @param secret: An string
 * @param guess: An string
 * @return: An string
 */

import "fmt"

func getHint (secret string, guess string) string {
    // write your code here
    n := len(secret)

    cnt := make(map[string]int)

    for _, s := range secret {
        cnt[string(s)]++
    }

    bulls := 0
    cows := 0

    for i := 0; i < n; i++ {
        gCnt, ok := cnt[string(guess[i])]
        if !ok && guess[i] != secret[i] {
            continue
        }

        if ok && gCnt == 0 {
            continue
        }

        if guess[i] == secret[i] {
            bulls++
        } else if ok && gCnt > 0 {
            cows++
        }
        cnt[string(guess[i])] = gCnt-1
    }

    return fmt.Sprintf("%dA%dB", bulls, cows)
}
