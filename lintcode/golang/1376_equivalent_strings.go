/**
 * @param s1: a string
 * @param s2: a string
 * @return: is s1 and s2 are equivalent
 */
func isEquivalentStrings (s1 string, s2 string) bool {
    // Write your code here
    l := len(s1)
    if l == 0 {
        return true
    }
    
    if l % 2 == 1 {
        return s1 == s2
    } else {
        a1 := s1[:l/2]
        a2 := s1[l/2:]
        b1 := s2[:l/2]
        b2 := s2[l/2:]
        
        if (isEquivalentStrings(a1, b1) && isEquivalentStrings(a2, b2) ||
            isEquivalentStrings(a1, b2) && isEquivalentStrings(a2, b1)) {
                return true
            }
    }
    
    return false
}

