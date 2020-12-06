
// AC

func findMissing2 (n int, str string) int {
    // write your code here
    ans := 0
    found := false
    dfs(0, n, str, map[int]bool{}, &ans, &found)
    return ans
}

func dfs(start,n int, s string, visited map[int]bool, ans *int, found *bool) {
    if start >= len(s) || *found {
        if !(*found) {
            cnt := 0
            curAnss := 0
            for i:= 1; i<=n;i++ {
                if v, ok := visited[i]; !ok || !v {
                    cnt++
                    curAnss = i
                }
            }
            if cnt == 1 {
                *found = true
                *ans = curAnss
            }
        }
        return
    }
    num := int(s[start] - '0')
    if num == 0 {
        return
    }
    i := start
    for num<=n {
        if !visited[num] {
            visited[num] = true
            dfs(i+1, n, s, visited, ans, found)
            visited[num] = false
        }
        if i<len(s)-1 {
            num = num*10 + int(s[i+1]-'0')
            i++
        } else {
            break
        }
    }
    return 
}


//my AC

/**
 * @param n: An integer
 * @param str: a string with number from 1-n in random order and miss one number
 * @return: An integer
 */
 
import (
    "strconv"
    //"fmt"
)
 
func findMissing2 (n int, str string) int {
    // write your code here
    v := make(map[int]bool)
    ret := -1
    
    dfs(n, str, 0, v, &ret)
    
    return ret
}

func dfs(n int, str string, index int, v map[int]bool, ret *int) {
    if index == len(str) {
        //fmt.Println(index)
        cnt := 0
        tmp := 0
        for i := 1; i <= n; i++ {
            //fmt.Println(str, i)
            if exist, ok := v[i]; !ok || (!exist) {
                cnt++
                tmp = i
            }
        }
        
        if cnt == 1 {
            *ret = tmp
        }
        return
    }
    
    if str[index] == '0' {
        return
    }
    
    for i := 1; i < 3; i++ {
        if index+i > len(str) {
            return
        }
        new_str := str[index:index+i]
        new_num, err := strconv.Atoi(new_str)
        
        if err != nil {
            return
        }
        if exist, ok := v[new_num]; ok && exist {
            continue
        }
        if new_num <= 0 || new_num > n {
            continue
        }
        //fmt.Println(new_str, new_num)
        v[new_num] = true
        
        dfs(n, str, index+i, v, ret)
        
        v[new_num] = false
    }
    
    return
}


