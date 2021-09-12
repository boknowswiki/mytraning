#!/usr/bin/python -t


# two pointer

# 双指针模式，左指针代表最小数（可以是负数）右指针代表最大数。由于可能是正负数夹杂在一块，所以需要定义专门寻找左右指针的下一个数的方法.
# 首先定义初始左指针和右指针为最右端，然后使用定义好的方法找到整个数组的最大数和最小数，以及相应指针的运动方向。如果数组都是正数，那么就是
# 普通的twoSum，左指针在最左端，右指针在最右端，相向移动。如果是正负数间杂，那么左右指针之一都可能在最左端和最右端之间某个位置。刚开始
# 两个指针都需要向左移动直到某个指针到达最左端，然后改变移动方向为向右移动。其他则是通用的方法，和小于目标值，移动左指针，否则右指针。
# 最后对得到的结果排序.由于最后的结果数目很小，这个排序时间对整个时间复杂度没有影响。O(n)时间，O(1)空间

class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def twoSumVII(self, nums, target):
        # write your code here
        n = len(nums)
        if n == 0:
            return []
        left = 0
        right = 0
        for i in range(n):
            if nums[i] > nums[right]:
                right = i
            if nums[i] <= nums[left]:
                left = i
        ret = []

        while nums[left] < nums[right]:
            if nums[left] + nums[right] < target:
                left = self.nextLeft(left, nums)
                if left == -1:
                    break
            elif nums[left] + nums[right] > target:
                right = self.nextRight(right, nums)
                if right == -1:
                    break
            else:
                tmp = [left, right]
                if left > right:
                    tmp[0], tmp[1] = tmp[1], tmp[0]
                ret.append(tmp)
                left = self.nextLeft(left, nums)
                if left == -1:
                    break

        return ret

    def nextLeft(self, left, nums):
        n = len(nums)
        if nums[left] < 0:
            for i in range(left-1, -1, -1):
                if nums[i] < 0:
                    return i
            for i in range(n):
                if nums[i] >= 0:
                    return i
            return -1
        for i in range(left+1, n):
            if nums[i] >= 0:
                return i

        return -1

    def nextRight(self, right, nums):
        n = len(nums)
        if nums[right] > 0:
            for i in range(right-1, -1,-1):
                if nums[i] >0:
                    return i
            for i in range(n):
                if nums[i] <= 0:
                    return i
            return -1
        for i in range(right+1, n):
            if nums[i] <= 0:
                return i
        return -1



type ByFirst []([]int)

func (a ByFirst) Len() int           { return len(a) }
func (a ByFirst) Less(i, j int) bool { return a[i][0] < a[j][0] }
func (a ByFirst) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }

func nextRight(nums []int, left int, right int, rtoLeft bool) (int, bool) {
	if rtoLeft {
		right--
		for ; right > 0 && nums[right] < 0; {
			right--
		}
		if right == 0 {
			rtoLeft = false
		}
	} else {
		right++
		for ; left != right && nums[right] > 0; {
			right++
		}
	}
	return right, rtoLeft
}

func nextLeft(nums[]int, left int, right int, ltoLeft bool) (int, bool) {
	if ltoLeft {
		left--
		for ; left > 0 && nums[left] > 0; {
			left--
		}
		if left == 0 {
			ltoLeft = false
		}
	} else {
		left++
		for ;left != right && nums[left] < 0; {
			left++
		}
	}
	return left, ltoLeft
}

func twoSumVII (nums []int, target int) [][]int {
	n := len(nums)
	result := make([]([]int), 0)
	if n <= 1 {
		return result
	}
	left, right, sum := n-1, n-1, 0
	ltoLeft, rtoLeft := true, true
	if nums[n-1] > 0 {
		left, ltoLeft = nextLeft(nums, left, right, ltoLeft)
	} else {
		right, rtoLeft = nextRight(nums, left, right, rtoLeft)
	}

	for right >= 0 && right < n && left >= 0 && left < n && left != right {
		sum = nums[left] + nums[right]
		if sum > target {
			right, rtoLeft = nextRight(nums, left, right, rtoLeft)
		} else if sum < target {
			left, ltoLeft = nextLeft(nums, left, right, ltoLeft)
		} else {
			var tmp []int
			if left < right {
				tmp = []int{left, right}
			} else {
				tmp = []int{right, left}
			}
			result = append(result, tmp)

			left, ltoLeft = nextLeft(nums, left, right, ltoLeft)
			if left == right {
				break
			}
			right, rtoLeft = nextRight(nums, left, right, rtoLeft)
			if left == right {
				break
			}
		}
	}
	sort.Sort(ByFirst(result))
	return result
}
