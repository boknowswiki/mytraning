/**
 * @param A: an array
 * @param S: the sum
 * @return: the number of non-empty subarrays
 */
func numSubarraysWithSum (A []int, S int) int {
    // Write your code here.
    ret := 0
    sumMap := make(map[int]int, len(A)+1)
    sumMap[0] = 1
    preSum := 0

    for i := range A {
        preSum += A[i]
        if preSum - S >= 0 {
            ret += sumMap[preSum-S]
        }
        sumMap[preSum]++
    }

    return ret
}
