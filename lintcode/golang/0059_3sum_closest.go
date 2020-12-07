/**
 * @param numbers: Give an array numbers of n integer
 * @param target: An integer
 * @return: return the sum of the three integers, the sum closest target.
 */
 
import "sort"

func threeSumClosest (numbers []int, target int) int {
    // write your code here
    if len(numbers) == 0 {
        return 0
    }
    
    sort.Ints(numbers)
    var ret int
    var sum int
    minDiff := target
    
    for index := range numbers {
        l := index+1
        r := len(numbers)-1

        for l < r {
            sum = numbers[index] + numbers[l] + numbers[r]
            
            if sum == target {
                return sum
            }
            
            if ret == 0 || abs(sum-target) < minDiff {
                minDiff = abs(sum-target)
                ret = sum
            }
            
            if sum > target {
                r--
            } else {
                l++
            }
        }
    }
    
    return ret
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}

