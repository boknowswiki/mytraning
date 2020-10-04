
//输出到的矩阵的列数永远是奇数 -- 对于所有子树, 即原矩阵的子矩阵也是奇数. 因为是奇数时, 左右子树才能平分列数. 一棵高度为 height 的二叉树对应的矩阵是 height * (2^{height} - 1)height∗(2
//​height
//​​ −1) 的.
//
//先 dfs 确定二叉树的高度, 然后定义字符串二维数组. 再次 dfs 把每一个节点的值填入二维数组即可. 第二次 dfs 的过程中需要记录以下信息:
//
//当前节点所在行, 列 -- 确定当前节点的值填入二维数组的哪个位置
//当前节点的子树的宽度 -- 确定该节点的左右子节点该填入的位置
//当前节点在 [row, col], 宽度是 width 时, 其左右子树的宽度均为 width / 2 - 1 (宽度永远是奇数), 左右子节点所在列与 col 的距离相同, 都是宽度的一半.
//
//总归, 两次dfs就可以解决这个问题.

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
