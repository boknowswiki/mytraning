
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
 * @return: Inorder in ArrayList which contains node values.
 */
func inorderTraversal (root *TreeNode) []int {
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
    
    *ret = append(*ret, node.Val)
    
    if node.Right != nil {
        helper(node.Right, ret)
    }
}


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
 * @return: Inorder in ArrayList which contains node values.
 */
func inorderTraversal (root *TreeNode) []int {
    // write your code here
    ret := make([]int, 0)
    if root == nil {
        return ret
    }
    
    stack := make([]*TreeNode, 0)
    cur := root
    
    for cur != nil {
        stack = append(stack, cur)
        cur = cur.Left
    }
    
    for len(stack) != 0 {
        cur = stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        ret = append(ret, cur.Val)
        if cur.Right != nil {
            node := cur.Right
            for node != nil {
                stack = append(stack, node)
                node = node.Left
            }
        }
    }
    
    return ret
}

