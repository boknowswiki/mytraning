package main

// heap

import (
	"fmt"
)

func heapify(a []int) {
	n := len(a)
	if n < 2 {
		return
	}

	/*
		for i := (n - 2) / 2; i >= 0; i-- {
			shiftDown(a, n, i)
		}
	*/

	for i := 0; i < n; i++ {
		shiftUp(a, i)
	}
}

func shiftUp(a []int, start int) {
	for {
		p := (start - 1) / 2
		if p >= 0 {
			if a[start] >= a[p] {
				break
			}
			a[start], a[p] = a[p], a[start]
			start = p
		} else {
			break
		}
	}

	return
}

func shiftDown(a []int, end int, start int) {
	for start < end {
		left := 2*start + 1
		right := 2*start + 2
		minIndex := start
		if left < end && a[left] < a[minIndex] {
			minIndex = left
		}
		if right < end && a[right] < a[minIndex] {
			minIndex = right
		}

		if start == minIndex {
			break
		}

		a[start], a[minIndex] = a[minIndex], a[start]
		start = minIndex
	}

	return
}

func main() {
	a := []int{3, 17, 5, 19, 21, 7}
	fmt.Println(a)
	heapPush(&a, 0)
	fmt.Println(a)
	heapPop(&a)
	fmt.Println(a)
}

func heapPush(a *[]int, val int) {
	*a = append(*a, val)
	shiftUp(*a, len(*a)-1)
}

func heapPop(a *[]int) {
	(*a)[0], (*a)[len(*a)-1] = (*a)[len(*a)-1], (*a)[0]
	*a = (*a)[:len(*a)-1]
	shiftDown(*a, len(*a), 0)
}
