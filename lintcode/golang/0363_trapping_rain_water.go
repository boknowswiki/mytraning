package main

// two pointers

// we may think of some way to do it in one iteration. From the figure in dynamic programming approach, notice that as long as \text{right\_max}[i]>\text{left\_max}[i]right_max[i]>left_max[i] (from element 0 to 6), the water trapped depends upon the left_max, and similar is the case when \text{left\_max}[i]>\text{right\_max}[i]left_max[i]>right_max[i] (from element 8 to 11). So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left). We must maintain \text{left\_max}left_max and \text{right\_max}right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.
// 
// Algorithm
// 
// Initialize \text{left}left pointer to 0 and \text{right}right pointer to size-1
// While \text{left}< \text{right}left<right, do:
// If \text{height[left]}height[left] is smaller than \text{height[right]}height[right]
// If \text{height[left]} \geq \text{left\_max}height[left]≥left_max, update \text{left\_max}left_max
// Else add \text{left\_max}-\text{height[left]}left_max−height[left] to \text{ans}ans
// Add 1 to \text{left}left.
// Else
// If \text{height[right]} \geq \text{right\_max}height[right]≥right_max, update \text{right\_max}right_max
// Else add \text{right\_max}-\text{height[right]}right_max−height[right] to \text{ans}ans
// Subtract 1 from \text{right}right.

// Time O(n), space O(1)

/**
 * @param heights: a list of integers
 * @return: a integer
 */
func trapRainWater(heights []int) int {
	// write your code here
	n := len(heights)
	if n == 0 || n == 1 {
		return 0
	}
	ret := 0

	leftMax := 0
	rightMax := 0
	left := 0
	right := n-1

	for left < right {
		if heights[left] < heights[right] {
			if heights[left] > leftMax {
				leftMax = heights[left]
			} else {
				ret += leftMax - heights[left]
			}
			left++
		} else {
			if heights[right] > rightMax {
				rightMax = heights[right]
			} else {
				ret += rightMax - heights[right]
			}
			right--
		}
	}

	return ret
}



// using stacks, monotonic stack

// we can use stack to keep track of the bars that are bounded by longer bars and hence, may store water. Using the stack, we can do the calculations in only one iteration.
// 
// We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, which means that the current bar is bounded by the previous bar in the stack. If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is bounded by the current bar and a previous bar in the stack, hence, we can pop it and add resulting trapped water to \text{ans}ans.
// 
// Algorithm
// 
// Use stack to store the indices of the bars.
// Iterate the array:
// While stack is not empty and \text{height[current]}>\text{height[st.top()]}height[current]>height[st.top()]
// It means that the stack element can be popped. Pop the top element as \text{top}top.
// Find the distance between the current element and the element at top of stack, which is to be filled. \text{distance} = \text{current} - \text{st.top}() - 1distance=current−st.top()−1
// Find the bounded height \text{bounded\_height} = \min(\text{height[current]}, \text{height[st.top()]}) - \text{height[top]}bounded_height=min(height[current],height[st.top()])−height[top]
// Add resulting trapped water to answer \text{ans} \mathrel{+}= \text{distance} \times \text{bounded\_height}ans+=distance×bounded_height
// Push current index to top of the stack
// Move \text{current}current to the next position

// Time O(n), space O(n)

/**
 * @param heights: a list of integers
 * @return: a integer
 */
func trapRainWater(heights []int) int {
	// write your code here
	n := len(heights)
	if n == 0 || n == 1 {
		return 0
	}
	ret := 0

	st := []int{}

	for cur := 0; cur < n; {
		//fmt.Println(st, len(st))
		for len(st) != 0 && heights[cur] > heights[st[len(st)-1]] {
			top := st[len(st)-1]
			st = st[:len(st)-1]
			if len(st) == 0 {
				break
			}
			dist := cur - st[len(st)-1] - 1
			depth := min(heights[cur], heights[st[len(st)-1]]) - heights[top]
			ret += dist * depth
		}
		st = append(st, cur)
		cur++
	}

	return ret
}


import (
	"fmt"
)

// dp or prefix.
//Find maximum height of bar from the left end upto an index i in the array \text{left\_max}left_max.
//Find maximum height of bar from the right end upto an index i in the array \text{right\_max}right_max.
//Iterate over the \text{height}height array and update ans:
//Add \min(\text{left\_max}[i],\text{right\_max}[i]) - \text{height}[i]min(left_max[i],right_max[i])−height[i] to \text{ans}ans
// time O(n), space O(n).

/**
 * @param heights: a list of integers
 * @return: a integer
 */
func trapRainWater(heights []int) int {
	// write your code here
	n := len(heights)
	if n == 0 || n == 1 {
		return 0
	}

	leftMax := []int{}
	rightMax := []int{}

	cur := 0
	for i := 0; i < n; i++ {
		cur = max(heights[i], cur)
		leftMax = append(leftMax, cur)
	}

	cur = 0
	for i := n - 1; i >= 0; i-- {
		cur = max(heights[i], cur)
		rightMax = append(rightMax, cur)
	}

	rightMax = reverse(rightMax)

	ret := 0
	for i := 0; i < n; i++ {
		ret += min(leftMax[i], rightMax[i]) - heights[i]
	}
	return ret
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func reverse(numbers []int) []int {
	for i := 0; i < len(numbers)/2; i++ {
		j := len(numbers) - i - 1
		numbers[i], numbers[j] = numbers[j], numbers[i]
	}
	return numbers
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	fmt.Println(trapRainWater(a))
}
