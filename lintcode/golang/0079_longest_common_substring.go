/**
 * @param A: A string
 * @param B: A string
 * @return: the length of the longest common substring.
 */
func longestCommonSubstring (A string, B string) int {
    // write your code here
    ret := 0
    
    for i := range A {
        for j := range B {
            dist := 0
            
            for i+dist < len(A) && j+dist<len(B) && A[i+dist] == B[j+dist] {
                dist++
                if dist > ret {
                    ret = dist
                }
            }
        }
    }
    
    return ret
}
