/**
 * @param words: a list of words
 * @param word1: a string
 * @param word2: a string
 * @return: the shortest distance between word1 and word2 in the list
 */

//import "fmt"
 
func shortestDistance (words []string, word1 string, word2 string) int {
    // Write your code here
    m := make(map[string]int)
    ret := len(words)
    
    for index := range words {
        if word1 == words[index] {
            m[word1] = index
        }
        if word2 == words[index] {
            m[word2] = index
        }
        
        if len(m) == 2 {
            ret = min(ret, abs(m[word2]- m[word1]))
        }
    }
    
    //fmt.Println(m, len(m))

    
    return ret
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
