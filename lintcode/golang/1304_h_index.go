import "sort"

func hIndex(citations []int) int {
    sort.Ints(citations)
    
    for k, v := range citations {
        if v >= len(citations)-k {
            return len(citations)-k
        }
    }
    
    return 0
}
