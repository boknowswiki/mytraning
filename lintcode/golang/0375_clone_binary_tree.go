

type TreeQueue struct {
    data []*TreeNode
}

func (s *TreeQueue) Empty() bool {
	return len(s.data) == 0
}

func (s *TreeQueue) Pop() {
	if len(s.data) == 0 {
		return
	}
	s.data = s.data[1:]
}

func (s *TreeQueue) Top() *TreeNode {
	if len(s.data) == 0 {
		return nil
	}
	return s.data[0]
}

func (s *TreeQueue) Push(node *TreeNode) {
	s.data = append(s.data, node)
}

/**
 * @param root: The root of binary tree
 * @return: root of new tree
 */
func cloneTree(root *TreeNode) *TreeNode {
	var rs *TreeNode
	queue1 := &TreeQueue{
		data: []*TreeNode{},
	}
	queue2 := &TreeQueue{
		data: []*TreeNode{},
	}
	if root == nil {
		return rs
	}
	rs = &TreeNode{}
	queue1.Push(root)
	queue2.Push(rs)
	for !queue1.Empty() {
		node := queue1.Top()
		cpNode := queue2.Top()
		cpNode.Val = node.Val

		queue1.Pop()
		queue2.Pop()
		if node.Left != nil {
			queue1.Push(node.Left)
			cpNode.Left = &TreeNode{}
			queue2.Push(cpNode.Left)

		}
		if node.Right != nil {
			queue1.Push(node.Right)
			cpNode.Right = &TreeNode{}
			queue2.Push(cpNode.Right)
		}
	}

	return rs
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
 * @param root: The root of binary tree
 * @return: root of new tree
 */
func cloneTree (root *TreeNode) *TreeNode {
    // write your code here
    if root == nil {
        return nil
    }
    
    node := &TreeNode {Val:root.Val}
    node.Left = cloneTree(root.Left)
    node.Right = cloneTree(root.Right)
    
    return node
}

