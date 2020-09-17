/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param s: the s' root
 * @param t: the t' root
 * @return: whether tree t has exactly the same structure and node values with a subtree of s
 */
func isSubtree (s *TreeNode, t *TreeNode) bool {
    // Write your code here
    if s == nil {
        return t == nil
    }
    
    if s.Val == t.Val && isSame(s, t) {
        return true
    }
    
    return isSubtree(s.Left, t) || isSubtree(s.Right, t)
}

func isSame (s *TreeNode, t *TreeNode) bool {
    if s == nil {
        return t == nil
    }
    
    if t == nil || s.Val != t.Val {
        return false
    }
    
    return isSame(s.Left, t.Left) && isSame(s.Right, t.Right)
}
