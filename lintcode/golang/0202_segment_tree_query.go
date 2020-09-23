/**
 * Definition of SegmentTreeNode:
 * type SegmentTreeNode struct {
 *     Start, End, Max int
 *     Left, Right     *SegmentTreeNode
 * }
 */

/**
 * @param root: The root of segment tree.
 * @param start: start value.
 * @param end: end value.
 * @return: The maximum number in the interval [start, end]
 */

const MaxInt = int(^uint(0) >> 1)
const MinInt = -MaxInt-1

func query (root *SegmentTreeNode, start int, end int) int {
    // write your code here
    if root == nil {
        return 0
    }
    
    if start == root.Start && end == root.End {
        return root.Max
    }
    
    mid := (root.Start+root.End)/2
    left := MinInt
    right := MinInt
    
    if start <= mid {
        if mid < end {
            left = query(root.Left, start, mid)
        } else {
            left = query(root.Left, start, end)
        }
    }
    
    if mid < end {
        if start <= mid {
            right = query(root.Right, mid+1, end)
        } else {
            right = query(root.Right, start, end)
        }
    }
    
    return max(left, right)
}

func max (a, b int) int {
    if a > b {
        return a
    }
    return b
}

/**
 * Definition of SegmentTreeNode:
 * type SegmentTreeNode struct {
 *     Start, End, Max int
 *     Left, Right     *SegmentTreeNode
 * }
 */

/**
 * @param root: The root of segment tree.
 * @param start: start value.
 * @param end: end value.
 * @return: The maximum number in the interval [start, end]
 */
func query (root *SegmentTreeNode, start int, end int) int {
    // write your code here
    if root == nil || start > end {
        return 0
    }
    
    if start <= root.Start && root.End <= end {
        return root.Max
    }
    
    return max(query(root.Left, start, end), query(root.Right, start, end))
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
