// non-recursive

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
 * @return: Preorder in ArrayList which contains node values.
 */
func preorderTraversal (root *TreeNode) []int {
    // write your code here
    ret := make([]int, 0)
    stack := make([]*TreeNode, 0)
    
    if root != nil {
        stack = append(stack, root)
    }
    
    for len(stack) != 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        
        ret = append(ret, node.Val)
        
        if node.Right != nil {
            stack = append(stack, node.Right)
        }
        if node.Left != nil {
            stack = append(stack, node.Left)
        }
    }
    
    return ret
}

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
 * @return: Preorder in ArrayList which contains node values.
 */
func preorderTraversal (root *TreeNode) []int {
    // write your code here
    ret := make([]int, 0)
    
    helper(root, &ret)
    
    return ret
}

func helper(node *TreeNode, ret *[]int) {
    if node != nil {
        *ret = append(*ret, node.Val)
        
        if node.Left != nil {
            helper(node.Left, ret)
        }
        if node.Right != nil {
            helper(node.Right, ret)
        }
    }
}
