/**
 * @param numbers: Give an array numbers of n integer
 * @return: Find all unique triplets in the array which gives the sum of zero.
 */

import "sort"
 
func threeSum (numbers []int) [][]int {
    // write your code here
    n := len(numbers)
    if n == 0 {
        return [][]int{}
    }
    
    sort.Ints(numbers)
    ret := [][]int{}
    
    for i := 0; i < n-2; i++ {
        if i != 0 && numbers[i] == numbers[i-1] {
            continue
        }
        
        left := i+1
        right := n-1
        
        for left < right {
            val := numbers[i] + numbers[left] + numbers[right]
            if val == 0 {
                ret = append(ret, []int{numbers[i], numbers[left], numbers[right]})
                left++
                right--
                for left < right && left > 0 && numbers[left] == numbers[left-1] {
                    left++
                }
                for left < right && right < n-1 && numbers[right] == numbers[right+1] {
                    right--
                }
            } else if val < 0 {
                left++
            } else {
                right--
            }
        }
    }
    
    return ret
}
