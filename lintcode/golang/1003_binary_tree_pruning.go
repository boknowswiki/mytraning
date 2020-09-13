/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root
 * @return: the same tree where every subtree (of the given tree) not containing a 1 has been removed
 */

//import "fmt"

func pruneTree (root *TreeNode) *TreeNode {
    // Write your code here
    dpp(&root)
    return root
}

func dpp(root **TreeNode) {
    if (*root) != nil {
        dpp(&((*root).Left))
        dpp(&((*root).Right))

        if (*root).Val == 0 && (*root).Left == nil && (*root).Right == nil {
            *root = nil
        }
    }
}
