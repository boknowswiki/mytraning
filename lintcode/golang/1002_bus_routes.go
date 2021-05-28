//hash and bfs

/**
 * @param routes:  a list of bus routes
 * @param S: start
 * @param T: destination
 * @return: the least number of buses we must take to reach destination
 */

import "fmt"

func numBusesToDestination (routes [][]int, S int, T int) int {
    // Write your code here
    stopToBus := make(map[int][]int)

    for i := range routes {
        for _, stop := range routes[i] {
            if _, ok := stopToBus[stop]; !ok {
                stopToBus[stop] = []int{}
            }
            stopToBus[stop] = append(stopToBus[stop], i)
        }
    }

    fmt.Println(stopToBus)

    q := []int{}
    vBus := make(map[int]bool)
    vStop := make(map[int]bool)
    cnt := 0
    q = append(q, S)
    vStop[S] = true

    for len(q) > 0 {
        l := len(q)

        for i := 0; i < l; i++ {
            stop := q[0]
            q = q[1:]
            if stop == T {
                return cnt
            }

            buses := stopToBus[stop]
            for j := range buses {
                if vBus[buses[j]] == true {
                    continue
                }
                vBus[buses[j]] = true
                for _, nextStop := range routes[buses[j]] {
                    if vStop[nextStop] == false {
                        vStop[nextStop] = true
                        q = append(q, nextStop)
                    }
                }
            }
        }
        cnt++
    }

    return -1
}

