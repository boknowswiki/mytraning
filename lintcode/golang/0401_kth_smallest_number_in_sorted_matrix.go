
// heap

/**
 * @param matrix: a matrix of integers
 * @param k: An integer
 * @return: the kth smallest number in the matrix
 */

import (
    "container/heap"
)

type Node struct {
    x, y, val int
}

type Nodes []*Node

func (n *Nodes) Len() int           {return len(*n)}
func (n *Nodes) Less(i, j int) bool {return (*n)[i].val < (*n)[j].val}
func (n *Nodes) Swap(i, j int)      {(*n)[i], (*n)[j] = (*n)[j], (*n)[i]}

func (n *Nodes) Push(x interface{}) {*n = append(*n, x.(*Node))}
func (n *Nodes) Pop() interface{} {
    m := len(*n)
    ret := (*n)[m-1]
    //(*n)[m-1] = nil
    (*n) = (*n)[:m-1]
    return ret
}

func (n *Nodes) Peek() interface{} {
    return (*n)[0]
}

func kthSmallest (matrix [][]int, k int) int {
    // write your code here
    n := len(matrix)
    m := len(matrix[0])

    hq := Nodes{}
    heap.Init(&hq)
    heap.Push(&hq, &Node{0, 0, matrix[0][0]})
    var dx = [2]int{0,1}
    var dy = [2]int{1,0}

    var hash [][] bool
    for i:= 0; i < n;i ++ {
    	var temp []bool
		for j := 0; j<m; j++ {
			temp = append(temp,false)
			//dp[i][j] = rand.Intn(10)
		}
		hash = append(hash,temp)
	}
    
    for i := 0; i < k-1; i++ {
        cur := heap.Pop(&hq).(*Node)
        //ret = cur.val
        for j := 0; j < 2; j++ {
            next_x := cur.x + dx[j]
            next_y := cur.y + dy[j]
            nextNode := &Node{next_x,next_y,0}
            if next_x < n && next_y < m && !hash[next_x][next_y] {
                hash[next_x][next_y] = true
                nextNode.val = matrix[next_x][next_y]
                heap.Push(&hq,nextNode)
            }
        }
    }

    ret := hq.Peek().(*Node).val
    return ret
}
