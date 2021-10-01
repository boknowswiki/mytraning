package main

import (
	"fmt"
)

// two pionters

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

/**
 * @param s: A string
 * @param k: An integer
 * @return: An integer
 */
func lengthOfLongestSubstringKDistinct(s string, k int) int {
	// write your code here
	n := len(s)
	if n < k {
		return n
	}

	d := make(map[uint8]int)
	ret := 0
	left := 0
	for right := 0; right < n; right++ {
		if val, ok := d[s[right]]; ok {
			d[s[right]] = val + 1
		} else {
			d[s[right]] = 1
		}
		//fmt.Println(d)
		for len(d) > k && left <= right {
			//fmt.Println("removing left ", s[left])
			d[s[left]]--
			if d[s[left]] == 0 {
				delete(d, s[left])
			}
			left++
		}
		ret = max(ret, right-left+1)
	}

	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := "eceba"
	b := 3
	fmt.Println(lengthOfLongestSubstringKDistinct(a, b))
}


/**
 * @param s: A string
 * @param k: An integer
 * @return: An integer
 */
func lengthOfLongestSubstringKDistinct (s string, k int) int {
    // write your code here
    n := len(s)
    if n < k {
        return n
    }
    
    m := make(map[byte]int)
    l := 0
    ret := 0
    
    for i := 0; i < n; i++ {
        c := s[i]
        if _, ok := m[c]; !ok {
            m[c] = 1
        } else {
            m[c]++
        }
        
        for len(m) > k {
            rc := s[l]
            m[rc]--
            if m[rc] == 0 {
                delete(m, rc)
            }
            l++
        }
        
        ret = max(ret, i-l+1)
    }
    
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
