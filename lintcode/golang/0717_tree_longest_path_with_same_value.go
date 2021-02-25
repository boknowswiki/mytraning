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


/**
 * @param A: as indicated in the description
 * @param E: as indicated in the description
 * @return: Return the number of edges on the longest path with same value.
 */
func LongestPathWithSameValue (A []int, E []int) int {
    // write your code here
    tree := make(map[int][]int)
    ret := 0
    
    for i := 0; i < len(E); i += 2 {
        a, b := E[i], E[i+1]
        tree[a] = append(tree[a], b)
        tree[b] = append(tree[b], a)
    }
    
    var dfs func(int, int, map[int][]int, []int) int
    dfs = func(node int, parent int, graph map[int][]int, a []int) int {
        if node == 0 {
            return 0
        }
        
        max_one, max_two := 0, 0
        
        for _, child := range graph[node] {
            if child != parent {
                val := dfs(child, node, graph, a)
                if a[node-1] == a[child-1] {
                    if 1+val > max_one {
                        max_two = max_one
                        max_one = 1+val
                    } else if 1+val > max_two {
                        max_two = 1+val
                    }
                }
            }
        }
        
        ret = max(ret, max_two+max_one)
        return max_one
    }
    dfs(1, 0, tree, A)
    
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
