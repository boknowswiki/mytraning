// time O(n)
// space O(1)

func myAtoi(s string) int {
    result := 0
    sign := 1
    index := 0
    n := len(s)

    // Skip leading whitespace
    for index < n && unicode.IsSpace(rune(s[index])) {
        index++
    }

    // Check for sign
    if index < n && (s[index] == '+' || s[index] == '-') {
        if s[index] == '-' {
            sign = -1
        }
        index++
    }

    // Read digits
    for index < n && s[index] >= '0' && s[index] <= '9' {
        digit := int(s[index] - '0')

        // Check for overflow
        if result > (math.MaxInt32-digit)/10 {
            if sign == 1 {
                return math.MaxInt32
            }
            return math.MinInt32
        }

        result = result*10 + digit
        index++
    }

    return result * sign
}
