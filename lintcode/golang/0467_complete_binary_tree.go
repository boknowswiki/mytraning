
//如果我们发现了NULL node 他一定要是最后一个NODE， return TRUE, 如果NULL node 后面还有非NULL node,这个tree一定不是 COMPLETE RETURN FALSE。 TIME O(N)


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
 * @return: true if it is a complete binary tree, or false.
 */
func isComplete (root *TreeNode) bool {
    // write your code here
    if root == nil {
        return true
    }
    
    var endNode bool
    
    q := make([]*TreeNode, 0)
    q = append(q, root)
    
    for len(q) != 0 {
        node := q[0]
        q = q[1:]
        if node == nil {
            endNode = true
        } else {
            if endNode == true {
                return false
            }
            
            q = append(q, node.Left)
            q = append(q, node.Right)
        }
    }
    
    return true
}
}
