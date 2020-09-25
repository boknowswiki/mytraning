// recursion

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root of binary tree.
 * @return: An integer
 */
func maxPathSum2 (root *TreeNode) int {
    // write your code here
    if root == nil {
        return 0
    }
    
    if root.Left == nil && root.Right == nil {
        return root.Val
    }
    
    left := maxPathSum2(root.Left)
    right := maxPathSum2(root.Right)
    
    return max(max(left, right), 0) + root.Val
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}


//bfs

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root of binary tree.
 * @return: An integer
 */
const MaxInt = int(^uint(0)>>1)
const MinInt = -MaxInt-1

type Node struct {
    treeNode *TreeNode
    sum int
}

func maxPathSum2 (root *TreeNode) int {
    // write your code here
    if root == nil {
        return 0
    }
    
    q := []Node{Node{treeNode: root, sum: root.Val}}
    ret := MinInt
    
    for len(q) != 0 {
        node := q[0]
        q = q[1:]
        if node.sum > ret {
            ret = node.sum
        }
        if node.treeNode.Left != nil {
            q = append(q, Node{treeNode: node.treeNode.Left, sum: node.sum + node.treeNode.Left.Val})
        }
        
        if node.treeNode.Right != nil {
            q = append(q, Node{treeNode: node.treeNode.Right, sum: node.sum + node.treeNode.Right.Val})
        }
    }
    
    return ret
}

