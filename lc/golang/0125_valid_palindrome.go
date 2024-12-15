//time O(n)
//space O(1)

func isPalindrome(s string) bool {
    ru := []rune(s)
    l := 0
    r := len(ru)-1
    for l < r {
        if !isAlphanumeric(ru[l])  {
            l = l + 1
            continue
        }
        if !isAlphanumeric(ru[r]) {
            r = r -1
            continue
        }
        
        if unicode.ToLower(ru[l]) != unicode.ToLower(ru[r]) {
            return false
        }
        l = l+1
        r = r-1
    }

    return true
}

func isAlphanumeric(c rune) bool {
    return unicode.IsLetter(c) || unicode.IsNumber(c)
}
