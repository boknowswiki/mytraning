/**
 * @param str: the string
 * @param dict: the dictionary
 * @return: return words which  are subsequences of the string
 */
func findWords (str string, dict []string) []string {
    // Write your code here.
    var ret []string
    n := len(str)
    if n == 0 {
        return ret
    }
    
    for _, d := range dict {
        var sIndex, dIndex = 0, 0
        
        for {
            if sIndex == len(str) || dIndex == len(d) {
                break
            }
            if str[sIndex] == d[dIndex] {
                dIndex += 1
            }
            if dIndex == len(d) {
                ret = append(ret, d)
                break
            }
            sIndex += 1
        }
    }
    
    return ret
}


/**
 * @param str: the string
 * @param dict: the dictionary
 * @return: return words which  are subsequences of the string
 */
func findWords (str string, dict []string) []string {
    n := len(str)
    res := make([]string, 0)
    if n == 0 {
        return res
    }
    cMap := make(map[byte][]int)
    for i := 0; i < len(str); i++ {
        c := str[i]
        cMap[c] = append(cMap[c], i)
    }
    
    for _, word := range dict {
        curPos := -1
        foundWord := true
        
        for j := 0; j < len(word); j++ {
            var posArr []int
            var found bool
            if posArr, found = cMap[word[j]]; !found {
                foundWord = false
                break;
            }
            tarPos := findPos(posArr, curPos)
            if tarPos == -1 {
                foundWord = false
                break;
            }
            curPos = tarPos    
        }
        if foundWord == true {
            res = append(res, word)
        }
    } 
    return res
}

func findPos (posArr []int, curPos int) int {
    for _, pos := range posArr {
        if pos > curPos {
            return pos
        }
    }
    return -1
}
