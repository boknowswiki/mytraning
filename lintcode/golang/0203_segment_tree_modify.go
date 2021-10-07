package main

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
 * @param root: The root of segment tree.
 * @param index: index.
 * @param value: value
 * @return: nothing
 */
func modify(root **SegmentTreeNode, index int, value int) {
	// write your code here
	if (*root).Start == (*root).End && (*root).Start == index {
		(*root).Max = value
		return
	}
	if (*root).Left != nil && ((*root).Left.Start <= index && (*root).Left.End >= index) {
		modify(&(*root).Left, index, value)
	}
	if (*root).Right != nil && ((*root).Right.Start <= index && (*root).Right.End >= index) {
		modify(&(*root).Right, index, value)
	}
	if (*root).Left != nil && (*root).Right != nil {
		(*root).Max = max((*root).Left.Max, (*root).Right.Max)
	} else if (*root).Left == nil && (*root).Right != nil {
		(*root).Max = (*root).Right.Max
	} else if (*root).Right == nil && (*root).Left != nil {
		(*root).Max = (*root).Left.Max
	}

	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {

}
