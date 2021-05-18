/**
 * @param tagList: The tag list.
 * @param allTags: All the tags.
 * @return: Return the answer
 */

import "fmt"

func getMinimumStringArray (tagList []string, allTags []string) int {
    // Write your code here
    tagListDic := make(map[string]bool)
    foundTagsDic := make(map[string]int)

    n := len(tagList)
    m := len(allTags)

    for i := 0; i < n; i++ {
        tagListDic[tagList[i]] = true
        foundTagsDic[tagList[i]] = 0
    }
    fmt.Println("tagdic: ", tagListDic)
    fmt.Println("china is in: ", tagListDic["china"])

    ret := m+1
    cnt := 0
    left, right := 0, -1

    for right < m {
        fmt.Println("left: ", left, "right: ", right)
        fmt.Println("left word: ", allTags[left])
        if cnt < n {
            right++
            fmt.Println("right word: ", allTags[right], "tagdic: ", tagListDic[allTags[right]])
            if right == m {
                break
            }
            if tagListDic[allTags[right]] == true {
                foundTagsDic[allTags[right]]++
                if foundTagsDic[allTags[right]] == 1 {
                    cnt++
                }
            }
            fmt.Println("foundTagDic: ", foundTagsDic, "cnt: ", cnt)
        } else {
            if tagListDic[allTags[left]] == true {
                foundTagsDic[allTags[left]]--
                if foundTagsDic[allTags[left]] == 0 {
                    cnt--
                }
            }
            left++
        }
        if cnt == n {
            ret = min(ret, right-left+1)
        }
    }

    if ret == m+1 {
        return -1
    }

    return ret
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
