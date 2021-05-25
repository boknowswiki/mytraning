
// hash

/**
 * @param s: 
 * @return: return a string
 */

import "fmt"
import "sort"
//import "strings"

func frequencySort (s string) string {
    // write your code here
    n := len(s)
    if n == 0 {
        return ""
    }

    d := make(map[string]int)
    var ret string

    for _, ss := range s {
        d[string(ss)]++
    }

    fmt.Println(d)

    dd := make(map[int][]string)
    cnt := []int{}
    for k, v := range d {
        if _, ok := dd[v]; !ok {
            dd[v] = []string{}
        }
        dd[v] = append(dd[v], k)
    }

    fmt.Println(dd)

    for k, _ := range dd {
        cnt = append(cnt, k)
    }
    fmt.Println(cnt)

    sort.Sort(sort.Reverse(sort.IntSlice(cnt)))

    fmt.Println(cnt)

    for _, c := range cnt {
        sort.Strings(dd[c])
        fmt.Println(c, dd[c])
        for _, v := range dd[c] {
            for i := 0; i < c; i++ {
                ret += string(v)
            }
        }
    }

    return ret
}

