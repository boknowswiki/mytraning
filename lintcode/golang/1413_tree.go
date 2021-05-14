
// hash table and bfs

/**
 * @param x: The x
 * @param y: The y
 * @param a: The a
 * @param b: The b
 * @return: The Answer
 */

import "fmt"

func tree (x []int, y []int, a []int, b []int) []int {
    // Write your code here
    graph := make(map[int][]int)
    parent := make(map[int]int)
    m := len(a)
    ret := []int{}

    n := len(x)
    for i , j := 0, 0; i < n && j < n; i, j = i+1, j+1 {
        if xx, ok := graph[x[i]]; ok {
            graph[x[i]] = append(xx, y[j])
        } else {
            graph[x[i]] = []int{y[j]}
        }

        if yy, ok := graph[y[j]]; ok {
            graph[y[j]] = append(yy, x[i])
        } else {
            graph[y[j]] = []int{x[i]}
        }
    }

    fmt.Println("graph: ", graph)

    q := []int{1}
    v := make(map[int]bool)
    v[1] = true
    parent[1] = 0

    for len(q) != 0 {
        level := []int{}

        for _, val := range q {
            for _, nei := range graph[val] {
                if v[nei] == true {
                    continue
                }
                v[nei] = true
                level = append(level, nei)
                parent[nei] = val
            }
        }
        q = level
    }

    fmt.Println("parent: ", parent)

    for i , j := 0, 0; i < m && j < m; i, j = i+1, j+1 {
        if parent[a[i]] == parent[b[j]] {
            ret = append(ret, 1)
        } else if parent[a[i]] == b[j] || parent[b[j]] == a[i] {
            ret = append(ret, 2)
        } else {
            ret = append(ret, 0)
        }
    }

    return ret
}

