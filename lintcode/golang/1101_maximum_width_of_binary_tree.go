
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
 * @param root: the root
 * @return: the maximum width of the given tree
 */

type record struct {
    node *TreeNode
    depth int
    index int
} 

func widthOfBinaryTree (root *TreeNode) int {
    // Write your code here
    if root == nil {
        return 0
    }
    
    q := make([]record, 0)
    q = append(q, record{node: root})
    var ret, curDepth, left int
    
    for len(q) != 0 {
        level := make([]record, 0)
        
        for _, r := range q {
            if r.node != nil {
                level = append(level, record{node: r.node.Left, depth: r.depth+1, index: r.index*2})
                level = append(level, record{node: r.node.Right, depth: r.depth+1, index: r.index*2+1})
                if curDepth != r.depth {
                    curDepth = r.depth
                    left = r.index
                }
                
                ret = max(ret, r.index-left+1)
            }
        }
        q = level
    }
    
    return ret
}

func max (a, b int ) int {
    if a > b {
        return a
    }
    return b
}


//dfs

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
 * @return: the maximum width of the given tree
 */

//import "fmt"

func widthOfBinaryTree (root *TreeNode) int {
    // Write your code here
    if root == nil {
        return 0
    }
    
    ret := 1
    q := make([]int, 0)
    
    var helper func(*TreeNode, int, int)
    helper = func (node *TreeNode, depth int , index int) {
        if node == nil {
            return
        }
        
        if len(q) == depth {
            q = append(q, index)
        }
        
        ret = max(ret, index - q[depth]+1)
        
        helper(node.Left, depth+1, index*2)
        helper(node.Right, depth+1, index*2+1)
        
        return
    }
    
    helper(root, 0, 1)
    
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

