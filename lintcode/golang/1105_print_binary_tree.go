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
 * @return: the binary tree in an m*n 2D string array
 */
 
import "math"
//import "fmt"
import "strconv"

func printTree (root *TreeNode) [][]string {
    // Write your code here
    if root == nil {
        return [][]string{}
    }
    
    var getDepth func (*TreeNode) float64
    
    getDepth = func (node *TreeNode) float64 {
        if node == nil {
            return 0
        }
        
        return (1 + max(getDepth(node.Left), getDepth(node.Right)))
    }
    
    row := getDepth(root)
    col := math.Pow(2, row)-1
    //fmt.Println(row, col)
    ret := make([][]string, int(row))
    for a := range ret {
        ret[a] = make([]string, int(col))
    }
    
    //fmt.Println(ret)
        
    var helper func (*TreeNode, float64, float64)
    helper = func (node *TreeNode, level, pos float64) {
        if node == nil {
            return
        }
        leftPad, space := math.Pow(2, (row-level-1))-1, math.Pow(2, (row-level))-1
        index := leftPad+pos*(space+1)
        ret[int(level)][int(index)] = strconv.Itoa(node.Val)
        helper(node.Left, level+1, float64(int(pos)<<1))
        helper(node.Right, level+1, float64((int(pos)<<1)+1))
    }
        
    helper(root, 0, 0)
    
    return ret
}

func max(a, b float64) float64 {
    if a > b {
        return a
    }
    return b
}
