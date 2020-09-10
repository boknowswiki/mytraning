/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root of the binary tree
 * @return: all root-to-leaf paths
 */
 
import "fmt"

func binaryTreePaths (root *TreeNode) []string {
    // write your code here
    var ret []string
    if root == nil {
        return []string{}
    }
    
    path := fmt.Sprintf("%v", root.Val)
    dfs(root, path, &ret)
    
    fmt.Println(ret)
    fmt.Printf("%T, %#v", ret, ret)
    return ret
}

func dfs(node *TreeNode, path string, ret *[]string) {
    
    if node.Left == nil && node.Right == nil {
        fmt.Println(path)
        *ret = append(*ret, path)
        return
    }
    
    if node.Left != nil {
        s := fmt.Sprintf("%v->%v", path, node.Left.Val)
        dfs(node.Left, s, ret)
    }
    if node.Right != nil {
        s := fmt.Sprintf("%v->%v", path, node.Right.Val)
        dfs(node.Right, s, ret)
    }
    
    return
}
