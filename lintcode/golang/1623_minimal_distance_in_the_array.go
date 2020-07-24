
/**
 * @param a: array a
 * @param b: the query array
 * @return: Output an array of length `b.length` to represent the answer
 */
func minimalDistance (a []int, b []int) []int {
    // Write your code here
    if len(a) == 0 {
        return nil
    }

    result := make([]int, len(b), len(b))
    QuickSortPartition(a)
    for k, v := range b {
        result[k] = cal(a, v)
    }

    return result
}

func cal(a []int, target int) int {
    low, high := 0, len(a)-1
    for low+1 < high {
        mid := low + (high-low)/2
        if a[mid] == target {
            return target
        }
        if a[mid] < target {
            low = mid
        } else {
            high = mid
        }
    }
    d1, d2 := target-a[low], a[high]-target
    if d1 < 0 {
        d1 *= -1
    }
    if d2 < 0 {
        d2 *= -1
    }
    if d1 <= d2 {
        return a[low]
    }

    return a[high]
}

func QuickSortPartition(data []int) {
    if len(data) < 2 {
        return
    }

    quickSortPartition(data, 0, len(data)-1)
}

func quickSortPartition(data []int, start, end int) {
    if start < end && end < len(data) && start > -1 {
        p := getPartition(data, start, end)
        quickSortPartition(data, start, p-1)
        quickSortPartition(data, p+1, end)
    }
}

func getPartition(data []int, start, end int) int {
    if data == nil || start < 0 || end >= len(data) || start > end {
        return -1
    }
    i, pivot := start-1, data[end]
    for j := start; j < end; j++ {
        if data[j] <= pivot {
            i++
            if i != j {
                Swap(data, i, j)
            }
        }
    }
    Swap(data, i+1, end) // Swap arr[i+1] and arr[high] (or pivot)

    return i + 1 // Pivot is at i + 1
}

func Swap(data []int, i, j int) {
    if data == nil || len(data) == 0 || i < 0 || j < 0 || i >= len(data) || j >= len(data) {
        return
    }
    temp := data[i]
    data[i] = data[j]
    data[j] = temp
}


/**
 * @param a: array a
 * @param b: the query array
 * @return: Output an array of length `b.length` to represent the answer
 */
 
import "sort"

func minimalDistance (a []int, b []int) []int {
    // Write your code here
    if len(a) == 0 {
        return nil
    }

    ret := make([]int, len(b), len(b))
    sort.Ints(a)
    for k, v := range b {
        ret[k] = cal(a, v)
    }

    return ret
}

func cal(a []int, target int) int {
    low, high := 0, len(a)-1
    for low+1 < high {
        mid := low + (high-low)/2
        if a[mid] == target {
            return target
        }
        if a[mid] < target {
            low = mid
        } else {
            high = mid
        }
    }
    d1, d2 := target-a[low], a[high]-target
    if d1 < 0 {
        d1 *= -1
    }
    if d2 < 0 {
        d2 *= -1
    }
    if d1 <= d2 {
        return a[low]
    }

    return a[high]
}

