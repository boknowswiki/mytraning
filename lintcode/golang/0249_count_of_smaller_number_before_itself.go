/**
 * @param A: an integer array
 * @return: A list of integers includes the index of the first number and the index of the last number
 */
 
import "math"
//import "fmt"

func countOfSmallerNumberII (A []int) []int {
    // write your code here
    n := len(A)
    if n == 0 || (n == 1 && A[0] == 0) {
        return []int{}
    }
    
    min, max := math.MaxInt64, math.MinInt64
    for _, a := range A {
        if a < min {
            min = a
        }
        if a > max {
            max = a
        }
    }
    
    root := buildSegTree(min, max)
    //fmt.Println(root)
    modifySegTreeIncr(root, A[0])
    
    
    ret := make([]int, n)
    
    for i := 1; i < n; i++ {
        ret[i] = querySegTree(root, min, A[i]-1)
        modifySegTreeIncr(root, A[i])
    }
    
    return ret
}

type Node struct {
    Start int
    End int
    Cnt int
    Left *Node
    Right *Node
}

func buildSegTree(start, end int) *Node {
    if start > end {
        return nil
    }
    if start == end {
        return &Node {
            Start: start,
            End: end,
        }
    }
    
    root := &Node {
        Start: start,
        End: end,
    }
    mid := start + (end-start)/2
    root.Left = buildSegTree(start, mid)
    root.Right = buildSegTree(mid+1, end)
    //root.Cnt = root.Left.Cnt + root.Right.Cnt
    return root
}

func modifySegTreeIncr(root *Node, val int) {
    if root == nil{
        return
    }
    if root.Start == root.End && (root.Start == val) {
        root.Cnt++
        return
    }
    
    //fmt.Println(root)
    mid := root.Start + (root.End - root.Start) / 2
    if val <= mid {
        modifySegTreeIncr(root.Left, val)
    } else {
        modifySegTreeIncr(root.Right, val)
    }
    l, r := 0, 0
    if root.Left != nil {
        l = root.Left.Cnt
    }
    if root.Right != nil {
        r = root.Right.Cnt
    }
    root.Cnt = l+r
    return
}

func querySegTree(root *Node, start, end int) int {
    if root == nil {
        return 0
    }
    if start < root.Start {
        start = root.Start
    }
    
    if end > root.End {
        end = root.End
    }
    
    if root.Start == start && root.End == end {
        return root.Cnt
    }
    
    mid := root.Start + (root.End - root.Start) / 2
    if end <= mid {
        return querySegTree(root.Left, start, end)
    }
    if start > mid {
        return querySegTree(root.Right, start, end)
    }
    
    return querySegTree(root.Left, start, root.Left.End) + querySegTree(root.Right, root.Right.Start, end)
}
