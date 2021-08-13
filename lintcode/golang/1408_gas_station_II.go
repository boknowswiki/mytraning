package main

// heap
//一个简单的写法。heap只需要对已经加入的gas排序，即可，所以不需要写comparator。
//然后，对于这个题目的test cases，distance其实已经是拍好序的，所以2元组排序也可以省略。
//剩下的就是核心的贪心code，比较简短容易理解。
//
//复杂度分析有点笨，欢迎流言指教:
//
//所有的元素都加入到heap，平摊复杂度O(n)，然后只需要弹出一个元素O(1)即可，整体是O(n)。
//所有元素依次加入到heap，然后依次弹出，heap大小为1，所以整体是O(n)。
//中间情况，平均有k个元素在heap中，建立堆为O(k)，最多加入弹出(n - k)次，总体为O(k + (n-k)logk) ~ O((n-k)logk)，如果k ~ n/2，最坏还是O(nlogn)。
//
import (
	"container/heap"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

/**
 * @param target: The target distance
 * @param original: The original gas
 * @param distance: The distance array
 * @param apply: The apply array
 * @return: Return the minimum times
 */
func getTimes(target int, original int, distance []int, apply []int) int {
	// Write your code here
	var ret int
	var index int

	maxHp := &IntHeap{}

	for original < target {
		for distance[index] <= original {
			heap.Push(maxHp, apply[index])
			index++
		}

		if maxHp.Len() == 0 {
			break
		}

		original += heap.Pop(maxHp).(int)
		ret++
	}

	if original >= target {
		return ret
	}
	return -1
}

// This example inserts several ints into an IntHeap, checks the minimum,
// and removes them in order of priority.
func main() {
	getTimes(25, 10, []int{10, 14, 20, 21}, []int{10, 5, 2, 4})
}
