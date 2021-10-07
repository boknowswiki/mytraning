package main

import "fmt"

// segment tree

/**
 * Definition of SegmentTreeNode:
 */
type SegmentTreeNode struct {
	Start, End, Max int
	Left, Right     *SegmentTreeNode
}

/**
 * Definition of SegmentTreeNode:
 * type SegmentTreeNode struct {
 *     Start, End, Max int
 *     Left, Right     *SegmentTreeNode
 * }
 */

/**
 * @param A: a list of integer
 * @return: The root of Segment Tree
 */
func build(A []int) *SegmentTreeNode {
	// write your code here
	root := helper(A, 0, len(A)-1)
	return root
}

func helper(a []int, start int, end int) *SegmentTreeNode {
	if start > end {
		return nil
	}
	if start == end {
		return &SegmentTreeNode{
			Start: start,
			End:   end,
			Max:   a[start],
		}
	}

	node := &SegmentTreeNode{
		Start: start,
		End:   end,
	}
	mid := (start + end) / 2
	left := helper(a, start, mid)
	right := helper(a, mid+1, end)
	if left != nil && right != nil {
		node.Max = max(left.Max, right.Max)
		node.Left = left
		node.Right = right
	} else if left == nil {
		node.Max = right.Max
		node.Right = right
	} else if right == nil {
		node.Max = left.Max
		node.Left = left
	}

	return node
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []int{3, 2, 1, 4}
	fmt.Println(build(a))
}
