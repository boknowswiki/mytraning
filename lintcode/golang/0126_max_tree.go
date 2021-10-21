package main

// stack
// time O(n)

import (
	"fmt"
)

// 算法：单调栈
// 思路
// 单调栈可以在O(n)的时间里跑出以每个元素作为最大/小值的最左/右端点下标。
// 基本过程：
// 单调栈的操作：以一个递减的单调栈为例，若栈为空或者栈顶元素大于当前元素则压入，否则弹出栈内比当前元素小的所有元素。
// 以序列{7， 2， 5， 3， 11， 9}为例，模拟一下实现过程。
// 第一步：栈为空，压入7。                                                  此时栈内：[7]
// 第二步：7比2大，压入2。                                                 此时栈内：[7, 2]
// 第三步：2比5小，弹出2，压入5。                                          此时栈内：[7, 5]
// 第四步：5比3大，压入3。                                                  此时栈内：[7, 5, 3]
// 第五步：3、5、7 比11小，弹出3、弹出5、弹出7，压入11。               此时栈内：[11]
// 第六步：11比9大，压入9 。                                                此时栈内：[11, 9]
// 在这个过程中可以发现，栈底元素是栈内元素中的最大值，而最后留在栈内的最底部的元素就是整个数组中的最大元素root。一个元素作为节点时的左儿子也就是左半边最大的值，是这个元素被压入栈时，栈弹出的最后一个元素；而右儿子也就是右半边最大的值，是这个元素的上面一个元素，因为递减的单调栈是从底部往顶部依次减小的。
// 具体实现：
// 从前往后依次遍历数组元素，对每个元素：
//
// 如果栈内有元素且元素小于当前元素，那么就需要依次弹出栈内比当前元素小的元素。在这个过程中记录最后一个被弹出的元素，这个元素就是当前元素的左儿子。
// 如果栈内有元素且栈顶元素大于当前元素，那么当前元素就是栈顶元素的右儿子。
// 最后压入当前元素。
// 所以我们很容易在这个过程中得到答案，也就是{11,7,9,#,5,#,#,2,3}。
// 复杂度
// 空间复杂度O(n)
// 时间复杂度O(n)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * @param A: Given an integer array with no duplicates.
 * @return: The root of max tree.
 */
func maxTree(A []int) *TreeNode {
	// write your code here
	n := len(A)
	if n == 0 {
		return nil
	}
	st := make([]*TreeNode, 0)

	for i := range A {
		node := &TreeNode{Val: A[i]}
		fmt.Println("num: ", A[i], "st: ", st)
		for len(st) != 0 && st[len(st)-1].Val < A[i] {
			node.Left = st[len(st)-1]
			st = st[:len(st)-1]
		}
		if len(st) != 0 {
			st[len(st)-1].Right = node
		}
		st = append(st, node)
	}
	return st[0]
}

func main() {
	a := []int{2, 5, 6, 0, 3, 1}
	fmt.Println(maxTree(a))
}
