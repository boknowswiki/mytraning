/**
 * @param A: as indicated in the description
 * @param E: as indicated in the description
 * @return: Return the number of edges on the longest path with same value.
 */
import "fmt"

type Node struct {
    Num     int
    Pare    int
    Step    int
}

func LongestPathWithSameValue (A []int, E []int) int {
    // write your code here
    n := len(A)
    tree := make(map[int][]int, 0)
    
    for i := 0; i < n-1; i++ {
        x, y := E[2*i]-1, E[2*i+1]-1
        tree[x] = append(tree[x], y)
        tree[y] = append(tree[y], x)
    }

    fmt.Println(tree)
    
    ret := make([]int, n)
    
    for i := 0; i < n; i++ {
        q := make([]Node, 0)
        q = append(q, Node{Num:i, Pare:-1, Step:0})
        for len(q) != 0 {
            node := q[0]
            q = q[1:len(q)]
            ret[i] = max(ret[i], node.Step)
            for nei := range tree[node.Num] {
                if (nei != node.Pare || node.Pare == -1) && (A[nei] == A[node.Num]) {
                    q = append(q, Node{Num:nei, Pare:node.Num, Step:node.Step+1,})
                }
            }
        }
    }
    
    var m int
    for v := range ret {
        if v > m {
            m = v
        }
    }
    
    return m
}

func max (a, b int) int {
    if a > b {
        return a
    }
    return b
}

