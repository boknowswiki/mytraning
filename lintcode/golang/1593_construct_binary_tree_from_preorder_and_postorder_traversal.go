/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param pre: 
 * @param post: 
 * @return: nothing
 */
func constructFromPrePost (pre []int, post []int) *TreeNode {
    //
    if len(pre) == 0 || len(post) == 0 {
        return nil
    }
    
    root := &TreeNode{ Val: pre[0],}
    
    if len(pre) == 1 {
        return root
    }
    
    var index int
    for i, node := range post {
        if node == pre[1] {
            index = i+1
            break
        }
    }
    
    left := constructFromPrePost(pre[1:index+1], post[:index])
    right := constructFromPrePost(pre[index+1:], post[index:len(post)-1])
    
    root.Left = left
    root.Right = right
    
    return root
}

