// not AC may due to lintcode main.go function issue.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: 
 * @return: nothing
 */

import "strconv"
import "strings"
import "fmt"

func serialize (root *TreeNode) string {
    //
    if root == nil {
        return ""
    }
    
    ret := make([]string, 0)
    q := make([]*TreeNode, 0)
    q = append(q, root)
    
    for len(q) != 0 {
        level := make([]*TreeNode, 0)
        allNil := true
        for _, node := range q {
            if node != nil {
                ret = append(ret, strconv.Itoa(node.Val))
                if node.Left != nil {
                    level = append(level, node.Left)
                    allNil = false
                } else {
                    level = append(level, nil)
                }
                if node.Right != nil {
                    level = append(level, node.Right)
                    allNil = false
                } else {
                    level = append(level, nil)
                }
            } else {
                ret = append(ret, "#")
            }
        }
        
        if ! allNil {
            q = level
        }
    }
    
    s:= strings.Join(ret, ",")
    
    fmt.Println(s)
    
    return s
}
/**
 * @param data: 
 * @return: nothing
 */
func deserialize (data string) *TreeNode {
    // 
    if len(data) == 0 {
        return nil
    }
    
    s := strings.Split(data, ",")
    fmt.Println(s)
    
    index := 0
    root := &TreeNode {
        //Val: strconv.Atoi(s[index]),
        Val: 1,
    }
    index++
    
    node := root
    
    for index < len(s) {
        left := index*2+1
        right := index*2+2
        if left >= len(s) || s[left] == "#" {
            node.Left = nil
        } else {
            node.Left = &TreeNode {
                //Val: strconv.Atoi(s[left]),
                Val: 1,
            }
        }
        if right >= len(s) || s[right] == "#" {
            node.Right = nil
        } else {
            node.Right = &TreeNode {
                //Val: strconv.Atoi(s[right]),
                Val: 1,
            }
        }
        index++
    }
    
    return root
}
