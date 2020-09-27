/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the given tree
 * @return: the tree after swapping
 */
 
const MaxInt = int(^uint(0)>>1)
const MinInt = -MaxInt-1

var pre *TreeNode
var first, second *TreeNode

func bstSwappedNode (root *TreeNode) *TreeNode {
    // write your code here
    if root == nil {
        return nil
    }
    
    pre = &TreeNode{Val: MinInt}
    
    dfs(root)
    
    if first != nil  && second != nil {
        tmp := first.Val
        first.Val = second.Val
        second.Val = tmp
    }
    
    return root
}

func dfs(node *TreeNode) {
    if node == nil {
        return
    }
    
    dfs(node.Left)
    
    if pre.Val > node.Val {
        if first == nil {
            first = pre
        }
        second = node
    }
    
    pre = node
    
    dfs(node.Right)
    
    return
}
