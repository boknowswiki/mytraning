
// hash

/**
 * @param nums: the given array
 * @param k: the given k
 * @param t: the given t
 * @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
 */
func containsNearbyAlmostDuplicate (nums []int, k int, t int) bool {
    // Write your code here
    n := len(nums)
    if n == 0 {
        return false
    }

    bucket := make(map[int]int)

    for i, v := range nums {
        bucketNum := v
        offset := 0
        if t != 0 {
            bucketNum = v/t
            offset = 1
        }

        for idx := bucketNum-offset; idx < bucketNum+offset+1; idx++ {
            if val, ok := bucket[idx]; ok {
                if abs(val - v) <= t {
                    return true
                }
            }
        }
        bucket[bucketNum] = v
        if len(bucket) > k {
            if t == 0 {
                delete(bucket, nums[i-k])
            } else {
                delete(bucket, nums[i-k]/t)
            }
        }
    }

    return false
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}

