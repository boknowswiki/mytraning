//heap
//这道题要想明白2个点
//
//你任意选K个工人，只要按照性价比最低工人为基础，按照比例去给剩下K-1个工人开工资，肯定是能满足条件的
//相通了第一点，那么我从所有工人里面去找到所有K个的组合，求一个最小的这道题是不是就做出来了呢，是的，暴力解可以这样做，肯定我们要继续优化，所以这里要想通第二点
//
//我们要从工人里面选K个，任意选，使得他们的工资总和最小，能想到什么，是不是想到了优先队列，我们维持一个大小为K的最大堆，那么这个堆按照什么来排呢？首先，对于堆里面的K个工人，我们要按照堆里面性价比最低的来给工资，总工资是所有quality 乘以这个性价比，要让这个总工资最小，也就是要让quality最小，所以堆里面存的是quality，最后一个问题，我怎么直到堆里面工人的最小的性价比啊？我们把工人按照性价比从大到小排序即可


import (
	"container/heap"
    "sort"
	"math"
)

type Worker struct {
	rate    float64
	idx     int
	quality int
}

// An IntHeap is a min-heap of ints.
type IntHeap []*Worker

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].quality > h[j].quality }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(*Worker))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

/**
 * @param quality: an array
 * @param wage: an array
 * @param K: an integer
 * @return: the least amount of money needed to form a paid group
 */
func mincostToHireWorkers(quality []int, wage []int, K int) float64 {
	// Write your code here
    n := len(quality)
    workers := make([]Worker, n)
	for i := range quality {
		workers[i] = Worker{
			float64(wage[i]) / float64(quality[i]),
			i,
			quality[i],
		}
	}
	sort.Slice(workers, func(i, j int) bool {
		return workers[i].rate < workers[j].rate
	})

	maxHeap := &IntHeap{}

	sum := 0
	res := 1E9
	for i := range workers {
	  heap.Push(maxHeap, &workers[i])
		sum += workers[i].quality
		if maxHeap.Len() == K+1 {
			sum -= heap.Pop(maxHeap).(*Worker).quality
			res = math.Min(res, workers[i].rate*float64(sum))
		} else {
			if maxHeap.Len() == K {
				res = math.Min(res, workers[i].rate*float64(sum))
			}
		}
	}
	return res

}

