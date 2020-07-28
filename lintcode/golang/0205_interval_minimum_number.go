/**
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

/**
 * @param A: An integer array
 * @param queries: An query list
 * @return: The result list
 */
 
type SegNode struct {
    Start, End, Min int
    Left, Right *SegNode
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func buildSeg(A[]int, start, end int) *SegNode {
    if start > end {
        return nil
    }
    
    if start == end {
        return &SegNode {
            Start: start,
            End: end,
            Min: A[start],
        }
    }
    
    root := &SegNode {
        Start: start,
        End: end,
    }
    
    mid := (start+end)/2
    root.Left = buildSeg(A, start, mid)
    root.Right = buildSeg(A, mid+1, end)
    root.Min = min(root.Left.Min, root.Right.Min)
    
    return root
}

func querySeg(node *SegNode, start, end int) int {
    if start > node.End || end < node.Start {
        return 1<<31
    }
    if start <= node.Start && end >= node.End {
        return node.Min
    }
    
    return min(querySeg(node.Left, start, end), querySeg(node.Right, start, end))
}

func intervalMinNumber (A []int, queries []*Interval) []int {
    // write your code here
    var ret []int
    n := len(A)
    if n == 0 {
        return ret
    }
    
    root := buildSeg(A, 0, len(A)-1)
    
    for _, q := range queries {
        ret = append(ret, querySeg(root, q.Start, q.End))
    }
    
    return ret
}

