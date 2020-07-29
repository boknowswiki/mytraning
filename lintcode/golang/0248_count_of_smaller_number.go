
/**
 * @param A: An integer array
 * @param queries: The query list
 * @return: The number of element in the array that are smaller that the given integer
 */
type SegNode struct {
    Start, End, Cnt int
    Left, Right *SegNode
}

func buildSeg (start, end int) *SegNode {
    if start > end {
        return nil
    }
    if start == end {
        return &SegNode {
            Start: start,
            End: end,
        }
    }
    
    root := SegNode {
        Start: start,
        End: end,
    }
    
    mid := (start+end)/2
    root.Left = buildSeg(start, mid)
    root.Right = buildSeg(mid+1, end)
    
    return &root
}

func modifySeg (node *SegNode, index int, val int) {
    if node == nil {
        return
    }
    
    if node.Start == node.End && node.Start == index {
        node.Cnt += val
        return
    }
    
    if node.Left != nil && node.Left.End >= index {
        modifySeg(node.Left, index, val)
    } else {
        modifySeg(node.Right, index, val)
    }
    
    if node.Left != nil && node.Right != nil  {
        node.Cnt = node.Left.Cnt + node.Right.Cnt
    } else if node.Left != nil {
        node.Cnt = node.Left.Cnt
    } else if node.Right != nil {
        node.Cnt = node.Right.Cnt
    }
    
    return
}

func querySeg (node *SegNode, start, end int) int {
    if start > node.End || end < node.Start {
        return 0
    }
    if start <= node.Start && end >= node.End {
        return node.Cnt
    }
    
    return querySeg(node.Left, start, end) + querySeg(node.Right, start, end)
}

func countOfSmallerNumber (A []int, queries []int) []int {
    // write your code here
    var ret []int 
    root := buildSeg(0, len(A)-1)
    
    for _, a := range A {
        modifySeg(root, a, 1)
    }
    
    for _, q := range queries {
        ret = append(ret, querySeg(root, 0, q-1))
    }
    
    return ret
}

/**
 * @param A: An integer array
 * @param queries: The query list
 * @return: The number of element in the array that are smaller that the given integer
 */

import "sort"

func countOfSmallerNumber (A []int, queries []int) []int {
    // write your code here
    var ret []int
    
    n := len(A)
    if n == 0 {
        return ret
    }

    sort.Ints(A)
    
    for _, q := range queries {
        index := lower(A, q)
        ret = append(ret, index+1)
    }
    
    return ret
}

func lower(a []int, t int) int {
    l := 0
    r := len(a)-1
    
    for l + 1 < r {
        mid := (l+r)/2
        if a[mid] >= t {
            r = mid
        } else {
            l = mid
        }
    }
    
    if a[r] < t {
        return r
    } else if a[l] < t {
        return l
    }
    return -1
}
