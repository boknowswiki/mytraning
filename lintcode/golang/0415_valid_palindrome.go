/**
 * @param s: A string
 * @return: Whether the string is a valid palindrome
 */
 
import (
    "strings"
    "unicode"
)

func isCharAlphanumeric (r rune) bool {
    if unicode.IsDigit(r) || unicode.IsLetter(r) {
        return true
    }
    
    return false
}

func isPalindrome (s string) bool {
    // write your code here
    n := len(s)
    if n == 0 || n == 1{
        return true
    }
    
    s = strings.ToLower(s)
    
    l := 0
    r := n-1
    
    for l < r {
        for l < r && !isCharAlphanumeric(rune(s[l])) {
            l++
        }
        
        for l < r && !isCharAlphanumeric(rune(s[r])) {
            r--
        }
        
        if l < r {
            if s[l] == s[r] {
                l++
                r--
            } else {
                return false
            }
        }
    }
    
    return true
}
