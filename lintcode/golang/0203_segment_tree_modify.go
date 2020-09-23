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
func modify (root **SegmentTreeNode, index int, value int)  {
    // write your code here
    if *root == nil {
        return
    }
    
    if (*root).Start == index && (*root).End == index {
        (*root).Max = value
        return
    }
    
    mid := ((*root).Start + (*root).End)/2
    
    if (*root).Start <= mid && index <= mid {
        modify(&(*root).Left, index, value)
    }
    
    if index <= (*root).End && index > mid {
        modify(&(*root).Right, index, value)
    }
    
    (*root).Max = max((*root).Left.Max, (*root).Right.Max)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
