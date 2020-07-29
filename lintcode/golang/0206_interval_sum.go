/**
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

/**
 * @param A: An integer list
 * @param queries: An query list
 * @return: The result list
 */
 
type SegNode struct {
    Start, End int 
    Total int64
    Left, Right *SegNode
}

func buildSeg (a []int, start, end int) *SegNode {
    if start > end {
        return nil
    }
    if start == end {
        return &SegNode {
            Start: start,
            End: end,
            Total: int64(a[start]),
        }
    }
    
    root := SegNode {
        Start: start,
        End: end,
    }
    
    mid := (start+end)/2
    root.Left = buildSeg(a, start, mid)
    root.Right = buildSeg(a, mid+1, end)
    root.Total = root.Left.Total + root.Right.Total
    
    return &root
}

func querySeg (node *SegNode, start, end int) int64 {
    if start > node.End || end < node.Start {
        return 0
    }
    if start <= node.Start && end >= node.End {
        return node.Total
    }
    
    return querySeg(node.Left, start, end) + querySeg(node.Right, start, end)
}

func intervalSum (A []int, queries []*Interval) []int64 {
    // write your code here
    var ret []int64
    
    root := buildSeg(A, 0, len(A)-1)
    
    for _, i := range queries {
        ret = append(ret, querySeg(root, i.Start, i.End))
    }
    
    return ret
}

