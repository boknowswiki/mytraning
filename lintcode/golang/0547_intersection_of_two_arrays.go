/**
 * @param nums1: an integer array
 * @param nums2: an integer array
 * @return: an integer array
 */
func intersection (nums1 []int, nums2 []int) []int {
    // write your code here
    h := make(map[int]bool)
    ret := make([]int, 0)
    
    for _, val := range nums1 {
        h[val] = true
    }
    
    for _, val := range nums2 {
        if h[val] {
            ret = append(ret, val)
            h[val] = false
        }
    }
    
    quickSort(&ret, 0, len(ret)-1)
    
    return ret
}

func quickSort(ret *[]int, start int, end int) {
    if start < end {
        part := getPart(ret, start, end)
        
        quickSort(ret, start, part-1)
        quickSort(ret, part+1, end)
    }
}

func getPart(ret *[]int, start int, end int) int {
    pivot := (*ret)[end]
    index := start
    
    for i:= start; i < end; i++ {
        if (*ret)[i] <= pivot {
            tmp := (*ret)[i]
            (*ret)[i] = (*ret)[index]
            (*ret)[index] = tmp
            index += 1
        }
    }
    
    tmp := (*ret)[end]
    (*ret)[end] = (*ret)[index]
    (*ret)[index] = tmp
    return index
}
