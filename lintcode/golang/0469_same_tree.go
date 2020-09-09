
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param a: the root of binary tree a.
 * @param b: the root of binary tree b.
 * @return: true if they are identical, or false.
 */
func isIdentical (a *TreeNode, b *TreeNode) bool {
    // write your code here
    if a == nil && b == nil {
        return true
    }
    if a != nil && b != nil {
        if a.Val == b.Val {
            return isIdentical(a.Left, b.Left) && isIdentical(a.Right, b.Right)
        }
    }
    
    return false
}



/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param a: the root of binary tree a.
 * @param b: the root of binary tree b.
 * @return: true if they are identical, or false.
 */
func isIdentical (a *TreeNode, b *TreeNode) bool {
    if a == nil && b == nil {
		return true
	}
	if a == nil && b != nil {
		return false
	}
	if a != nil && b == nil {
		return false
	}
	if a.Val != b.Val {
		return false
	}
	stack_A := []*TreeNode{a}
	stack_B := []*TreeNode{b}
	for true {
		if len(stack_A) == 0 || len(stack_B) == 0 {
			break
		}
		tmp_A := stack_A[len(stack_A) - 1]
		tmp_B := stack_B[len(stack_B) - 1]
		stack_A = stack_A[:len(stack_A) - 1]
		stack_B = stack_B[:len(stack_B) - 1]
		if tmp_A.Left != nil && tmp_B.Left == nil || tmp_A.Left == nil && tmp_B.Left != nil {
			return false
		}else if tmp_A.Left != nil && tmp_B.Left != nil {
			if tmp_A.Left.Val != tmp_B.Left.Val {
				return false
			}
			stack_A = append(stack_A, tmp_A.Left)
			stack_B = append(stack_B, tmp_B.Left)
		}
		if tmp_A.Right != nil && tmp_B.Right == nil || tmp_A.Right == nil && tmp_B.Right != nil {
			return false
		}else if tmp_A.Right != nil && tmp_B.Right != nil {
			if tmp_A.Right.Val != tmp_B.Right.Val {
				return false
			}
			stack_A = append(stack_A, tmp_A.Right)
			stack_B = append(stack_B, tmp_B.Right)
		}
	}
	if len(stack_A) != 0 || len(stack_B) != 0 {
		return false
	}
	return true
}
