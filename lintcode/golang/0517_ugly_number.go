
/**
 * @param num: An integer
 * @return: true if num is an ugly number or false
 */
func isUgly (num int) bool {
    // write your code here
    primeFactors := []int{2, 3, 5}

    index := 0

    for num > 1 && index < len(primeFactors) {
        if num % primeFactors[index] == 0 {
            num /= primeFactors[index]
        } else {
            index++
        }
    }

    return num == 1
}
