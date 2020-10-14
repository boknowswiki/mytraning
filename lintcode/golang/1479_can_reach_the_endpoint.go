//don't know why it has errors

/**
 * @param map: the map
 * @return: can you reach the endpoint
 */

type direct struct {
    x int
    y int
}

func reachEndpoint (map [][]int) bool {
    // Write your code here
    m := len(map)
    n := len(map[0])
    
    v := make(map[][]int, 0)
    for i := 0; i < m; i++ {
        v[i] := make([]int, n)
    }
    
    d := []direct{{0,1},{0,-1},{1,0},{-1,0}}
    q := make([]direct, 0)
    q = append(q, direct{0,0})
    for len(q) != 0 {
        p := q[0]
        q = q[1:len(q)]
        
        for _, dd := range d {
            cx := p.x + dd.x
            cy := p.y + dd.y
            if cx >= 0 && cx < m && cy >= 0 && cy < n {
                if map[cx][cy] == 9 {
                    return true
                }
                if map[cx][cy] == 1 && v[cx][cy] == false {
                    q = append(q, direct{cx, cy})
                    v[cx][cy] = true
                }
            }
        }
    }
    
    return false
}

