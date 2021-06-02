//hash and sort

/**
 * @param mapping: a list of integer
 * @param nums: a list of string
 * @return: return array of original values
 */

import "sort"

type Node struct {
    num string
    pos int
    realNum string
}

type NodeSlice []Node


func (nodeList NodeSlice) Len() int {
	return len(nodeList)
}

func (nodeList NodeSlice) Less(i, j int) bool {
	if len(nodeList[i].realNum) != len(nodeList[j].realNum) {
		return len(nodeList[i].realNum) < len(nodeList[j].realNum)
	}
	if nodeList[i].realNum != nodeList[j].realNum {
		return nodeList[i].realNum < nodeList[j].realNum
	}
	return nodeList[i].pos < nodeList[j].pos
}

func (nodeList NodeSlice) Swap(i, j int) {
	nodeList[i], nodeList[j] = nodeList[j], nodeList[i]
}

func strangeSort (mapping []int, nums []string) []string {
    // write your code here
    numMap := make(map[int]int)
    for i, v := range mapping {
        numMap[v] = i
    }

    var numSlice NodeSlice

    for i, num := range nums {
        var realSum []rune
        for _, v := range []rune(num) {
            tch := (rune)(numMap[(int(v)-48)] + 48)
			if len(realSum) == 0 && tch == 48 {
				continue
			}
			realSum = append(realSum, tch)
        }
        
        realN := string(realSum)
        node := Node {
            num: num,
            pos: i,
            realNum: realN,
        }
        numSlice = append(numSlice, node)
    }

    sort.Sort(numSlice)

	var ret []string
	for _, num := range numSlice {
		ret = append(ret, num.num)
	}
	return ret
}


