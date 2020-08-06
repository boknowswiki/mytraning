import "fmt"

type test struct {
    inter []int
    index int
}


func findRightInterval(intervals [][]int) []int {
    ordered := make([]test, len(intervals))
    fmt.Println(ordered)
    
    for k, v := range intervals {
        ordered[k].inter = v
        ordered[k].index = k
    }
    
    fmt.Println(ordered)
    sort.Slice(ordered, func(i, j int) bool { return ordered[i].inter[0] < ordered[j].inter[0] })
    fmt.Println(ordered)
    
    ret := make([]int, len(intervals))
    
    for k, v := range ordered {
        inter := v.inter
        left := k+1
        right := len(ordered)-1
        
        for left < right {
            mid := (left+right)/2
            if ordered[mid].inter[0] < inter[1] {
                left = mid+1
            } else {
                right = mid
            }
        }   
        if left < len(ordered) && ordered[left].inter[0] >= inter[1] {
            ret[v.index] = ordered[left].index
        } else {
            ret[v.index] = -1
        }
    }
    return ret
}
