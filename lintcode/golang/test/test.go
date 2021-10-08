package main

import "fmt"

// segment tree

const MaxUint = ^uint(0)
const MaxInt = int(MaxUint >> 1)

type segNode struct {
	Start, End, Min int
	Left, Right     *segNode
}

/**
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */
type Interval struct {
	Start, End int
}

/**
 * @param A: An integer array
 * @param queries: An query list
 * @return: The result list
 */
func intervalMinNumber(A []int, queries []*Interval) []int {
	// write your code here
	segTree := build(A)

	ret := []int{}

	for i := range queries {
		ret = append(ret, query(segTree, queries[i].Start, queries[i].End))
	}

	return ret
}

func build(a []int) *segNode {
	root := helper(a, 0, len(a)-1)
	return root
}

func helper(a []int, start, end int) *segNode {
	if start > end {
		return nil
	}
	if start == end {
		return &segNode{
			Start: start,
			End:   end,
			Min:   a[start],
		}
	}
	node := &segNode{
		Start: start,
		End:   end,
	}
	mid := (start + end) / 2
	node.Left = helper(a, start, mid)
	node.Right = helper(a, mid+1, end)
	if node.Left != nil && node.Right != nil {
		node.Min = min(node.Left.Min, node.Right.Min)
	}
	fmt.Println(node, node.Left, node.Right)

	return node
}

func query(root *segNode, start, end int) int {
	if root.Start == start && root.End == end {
		return root.Min
	}

	mid := (root.Start + root.End) / 2
	left := MaxInt
	right := MaxInt
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

	return min(left, right)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	a := []int{1, 2, 7, 8, 5}
	q := []*Interval{
		&Interval{Start: 1, End: 2},
		&Interval{Start: 0, End: 4},
		&Interval{Start: 2, End: 4},
	}
	fmt.Println(intervalMinNumber(a, q))
}
