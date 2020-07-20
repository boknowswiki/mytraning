// recursive

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: A Tree
 * @return: Postorder in ArrayList which contains node values.
 */
func postorderTraversal (root *TreeNode) []int {
    // write your code here
    ret := make([]int, 0)
    if root == nil {
        return ret
    }
    
    helper(root, &ret)
    
    return ret
}

func helper(node *TreeNode, ret *[]int) {
    if node.Left != nil {
        helper(node.Left, ret)
    }
    if node.Right != nil {
        helper(node.Right, ret)
    }
    
    *ret = append(*ret, node.Val)
}

//non-recursive

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: A Tree
 * @return: Postorder in ArrayList which contains node values.
 */
func postorderTraversal (root *TreeNode) []int {
    // write your code here
    ret := make([]int, 0)
    if root == nil {
        return ret
    }
    
    stack := make([]*TreeNode, 0)
    var lastVisit *TreeNode
    
    for root != nil || len(stack) != 0 {
        for root != nil {
            stack = append(stack, root)
            root = root.Left
        }
        
        node := stack[len(stack)-1]
        if node.Right == nil || node.Right == lastVisit {
            stack = stack[:len(stack)-1]
            ret = append(ret, node.Val)
            lastVisit = node
        } else {
            root = node.Right
        }
    }
    
    
    return ret
}

