/**
 * @param nums: an integer array
 * @param k: An integer
 * @return: the top k largest numbers in array
 */
import "container/heap"

type intHeap []int

func (h intHeap) Len() int           { return len(h) }
func (h intHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h intHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *intHeap) Push(x interface{}) {
    // Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func topk(nums []int, k int) []int {
    // write your code here
    n := len(nums)
    if k <= 0 {
        return []int{}
    }
	h := intHeap(nums)
	heap.Init(&h)
	if k > n {
	    k = n
	}
	ret := make([]int, k)
	
	for i := 0; i < k; i++ {
		ret[i] = heap.Pop(&h).(int)
	}
	return ret
}
