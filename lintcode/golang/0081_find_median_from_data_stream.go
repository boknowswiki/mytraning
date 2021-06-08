
// heap and data stream
// lintcode issue, not AC, but should be correct.

import "container/heap"



type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
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

var minHeap *IntHeap = &IntHeap{}
var maxHeap *IntHeap = &IntHeap{}
var mid int
var isFirst bool = true
func init() {
    heap.Init(minHeap)
    heap.Init(maxHeap)
}

/**
 * @param val: An integer
 * @return: nothing
 */
func add (val int)  {
    // write your code here
    if isFirst {
        heap.Push(maxHeap, -val)
        mid = -(*maxHeap)[0]
        return
    }
    if val <= mid {
        heap.Push(maxHeap, -val)
    } else {
        heap.Push(minHeap, val)
    }

    if len(*maxHeap) > len(*minHeap)+1 {
        heap.Push(minHeap, -(heap.Pop(maxHeap).(int)))
    }
    if len(*maxHeap) < len(*minHeap) {
        heap.Push(maxHeap, (-heap.Pop(minHeap).(int)))
    }

    mid = -(*maxHeap)[0]
    return
}
/**
 * @return: return the median of the data stream
 */
func getMedian () int {
    // write your code here
    return mid
}









// from other's solution

type MinHeap struct {
    n    []interface{}
	l    int
	Less func(a, b interface{}) int
}

func NewMinHeap(n int, f func(a, b interface{}) int) *MinHeap {
	cap := 1
	for cap < (1<<31-1)/2 && cap < n {
		cap *= 2
	}
	return &MinHeap{
		n:    make([]interface{}, cap, cap),
		l:    0,
		Less: f,
	}
}

func (h *MinHeap) Push(v interface{}) {
	// dynamic expand
	i := h.l
	h.n[i] = v

	for i > 0 {
		f := i / 2
		if h.Less(h.n[f], h.n[i]) >= 0 {
			break
		}
		h.n[f], h.n[i] = h.n[i], h.n[f]
		i = f
	}
	h.l++
}

func (h *MinHeap) Pop() interface{} {
	if h.l <= 0 {
		return nil
	}

	r := h.n[0]
	i := 0
	h.n[0] = h.n[h.l-1]

	for {
		j := 2 * i
		if j > h.l-1 {
			break
		}
		if j+1 <= h.l-1 && h.Less(h.n[j+1], h.n[j]) >= 0 {
			j = j + 1
		}
		if h.Less(h.n[i], h.n[j]) >= 0 {
			break
		}
		h.n[i], h.n[j] = h.n[j], h.n[i]
		i = j
	}

	h.l--
	return r
}

func (h *MinHeap) Peek() interface{} {
	if h.l <= 0 {
		return nil
	}
	return h.n[0]
}

func (h *MinHeap) Len() int {
	return h.l
}

func (h *MinHeap) isEmpty() bool {
	return h.l == 0
}

func medianII(nums []int) []int {
	h1 := NewMinHeap(len(nums), func(a, b interface{}) int {
		na, _ := a.(int)
		nb, _ := b.(int)
		return na - nb
	})
	h2 := NewMinHeap(len(nums), func(a, b interface{}) int {
		na, _ := a.(int)
		nb, _ := b.(int)
		return nb - na
	})

	checkBalance := func() bool {
		return h1.Len() == h2.Len() || h1.Len() == h2.Len()+1
	}

	res := make([]int, 0, len(nums))
	for i := 0; i < len(nums); i++ {
		if h1.isEmpty() {
			h1.Push(nums[i])
		} else {
			top := h1.Peek().(int)
			if nums[i] <= top {
				h1.Push(nums[i])
			} else {
				h2.Push(nums[i])
			}
		}
		// balance
		if checkBalance() {
			res = append(res, h1.Peek().(int))
			continue
		}
		for {
			if h1.Len() > h2.Len() {
				h2.Push(h1.Pop())
			} else {
				h1.Push(h2.Pop())
			}
			if checkBalance() {
				res = append(res, h1.Peek().(int))
				break
			}
		}
	}
	return res
}


// from other's solution

/**
 * @param nums: A list of integers
 * @return: the median of numbers
 */
func medianII (nums []int) []int {
    // write your code here
    res := make([]int, 0)
    res = append(res, nums[0])
    
    left, right := make([]int, 0), make([]int, 0)
    mid := nums[0]

    for i := 1; i < len(nums); i++ {
        if nums[i] < mid {
            left = append(left, nums[i])
            genHeap(left, "left")
        } else {
            right = append(right, nums[i])
            genHeap(right, "right")
        }

        if len(left) > len(right) {
            right = append(right, mid)
            swap(right, 0, len(right) - 1)
            mid = left[0]
            left = left[1:]
            genHeap(left, "left")
        } 

        if len(left) < len(right) - 1 {
            left = append(left, mid)
            swap(left, 0, len(left) - 1)
            mid = right[0]
            right = right[1:]
            genHeap(right, "right")
        }
        res = append(res, mid)
    }

    return res

}



func genHeap(list []int, t string) {
    n := len(list) - 1
    for i := n / 2; i >= 0; i-- {
        if t == "left" {
            heapifyMax(list, n, i)
        } else {
            heapifyMin(list, n, i)
        }
    }
    return
}

func heapifyMax(list []int, n, i int) {
    c1 := i * 2 + 1
    c2 := i * 2 + 2
    MAX := i
    if c1 <= n && list[MAX] < list[c1] {
        MAX = c1
    }
    if c2 <= n && list[MAX] < list[c2] {
        MAX = c2
    }
    if MAX != i {
        swap(list, MAX, i)
        heapifyMax(list, n, MAX)
    }
    return
}

func heapifyMin(list []int, n, i int) {
    c1 := i * 2 + 1
    c2 := i * 2 + 2
    MIN := i
    if c1 <= n && list[c1] < list[MIN] {
        MIN = c1
    }
    if c2 <= n && list[c2] < list[MIN] {
        MIN = c2
    }
    if MIN != i {
        swap(list, MIN, i)
        heapifyMax(list, n, MIN)
    }
    return
}

func swap(list []int, a, b int) {
    temp := list[a]
    list[a] = list[b]
    list[b] = temp
    return
}
