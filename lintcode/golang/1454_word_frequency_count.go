/**
 * @param s: The string s
 * @param excludeList: The excludeList
 * @return: Return the most frequent words
 */

import (
    "strings"
    "sort"
)

func getWords (s string, excludeList []string) []string {
    // Write your code here
    n := len(s)
    ret := []string{}
    if n == 0 {
        return ret
    }

    ed := make(map[string]bool)
    d := make(map[string]int)

    for _, word := range excludeList {
        ed[word] = true
    }

    max_count := 0
    s = strings.ToLower(s) + " "
    str := ""
    for _, ch := range s {
        if ch >= 'a' && ch <= 'z' {
            str += string(ch)
        } else {
            if str != "" {
                if ed[str] == false {
                    d[str] += 1
                    if d[str] > max_count { max_count = d[str] }
                }
                str = ""
            }
        }
    }

    for str := range d {
        if d[str] == max_count {
            ret = append(ret, str)
        }
    }
    sort.Strings(ret)
    return ret


}

