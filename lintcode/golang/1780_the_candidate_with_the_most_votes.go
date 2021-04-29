/**
 * @param votes: The array of names of candidates in the election.
 * @return: The name of the candidate who has the most votes.
 */

package main

import "fmt"

func main(){
   votes := []string{"John", "Johnny", "Jackie", "Johnny", "John", "Jackie", "Jamie", "Jamie", "John","Johnny", "Jamie", "Johnny", "John"}

    fmt.Println("best is ", candidateWithTheMostVotes(votes))
}

func candidateWithTheMostVotes (votes []string) string {
    // Write your code here
    b := make(map[string]int)

    for _, v := range votes {
        fmt.Println(v)
        if val, ok := b[v]; ok {
            b[v] = val+1
        } else {
            b[v] = 1
        }
    }

    fmt.Println(b)
    maxCnt := 0
    var ret string
    for k, v := range b {
        if v > maxCnt || (v == maxCnt && k < ret) || ret == "" {
            maxCnt = v
            ret = k
        }
    }

    return ret
}

