// time O(n)
// space O(1)

func twoSum(numbers []int, target int) []int {
    l := 0
    r := len(numbers)-1
    for l < r {
        if numbers[l] + numbers[r] == target {
            return []int{l+1, r+1}
        } else if numbers[l] + numbers[r] > target {
            r = r-1
        } else{
            l = l+1
        }
    }

    return []int{-1, -1}
}


// time O(nlogn)
// space O(1)

func bsearch(numbers []int, target int, start int) int {
    end := len(numbers)-1

    for start < end {
        mid := (start+end)/2
        if target == numbers[mid] {
            return mid
        } else if target > numbers[mid] {
            start = mid+1
        } else {
            end = mid-1
        }
    }

    if (start == end) && (target == numbers[start]) {
        return start
    }
    return -1
}

func twoSum(numbers []int, target int) []int {
    for i := 0; i < len(numbers); i++ {
        j := bsearch(numbers, target - numbers[i], i+1)
        if j != -1 {
            return []int {i+1, j+1}
        }
    }

    return []int{-1, -1}
}
