/**
 * @param logs: the logs
 * @return: the log after sorting
 */

import "strings"
 
func logSort (logs []string) []string {
    // Write your code here
    //l := len(logs)
    logNum, logStr := make([]string, 0), make([]string, 0)
    
    for i := range logs {
        if isContentNum(logs[i]) {
            logNum = append(logNum, logs[i])
        } else {
            logStr = append(logStr, logs[i])
        }
    }
    
    sortByContent(logStr, 0, len(logStr)-1)
    
    for j := 0; j < len(logStr); {
        content := getContent(logStr[j])
        k := j + 1
        for ; k < len(logStr) && content == getContent(logStr[k]); k++ {
        }
        sortByID(logStr, j, k - 1)
        j = k
    }
    
    return append(logStr, logNum...)
}

func sortByID(logs []string, start, end int) {
    if start < 0 || end >= len(logs) || start >= end {
        return
    }
    p := getPartitionByID(logs, start, end)
    sortByID(logs, start, p - 1)
    sortByID(logs, p + 1, end)
}

func getPartitionByID(logs []string, start, end int) int {
    if start < 0 || end >= len(logs) || start >= end {
        return -1
    }
    pivot := getID(logs[end])
    i := start - 1
    for j := start; j < end; j++ {
        if getID(logs[j]) <= pivot {
            i++
            if j != i {
                logs[j], logs[i] = logs[i], logs[j]
            }
        }
    }
    logs[i + 1], logs[end] = logs[end], logs[i + 1]
    
    return i + 1
}

func sortByContent(logStr []string, start, end int) {
    if start < end {
        part := getPartByContent(logStr, start, end)
        sortByContent(logStr, start, part-1)
        sortByContent(logStr, part+1, end)
    }
}

func getPartByContent(logStr []string, start, end int) int {
    pivot := getContent(logStr[end])
    index := start
    
    for i := start; i < end; i++ {
        if getContent(logStr[i]) < pivot {
            logStr[i], logStr[index] = logStr[index], logStr[i]
            index++
        }
    }
    
    logStr[index], logStr[end] = logStr[end], logStr[index]
    return index
}

func isContentNum(s string) bool {
    for i := strings.Index(s, " ") + 1; i < len(s); i++ {
        if s[i] == ' ' {
            continue
        }
        if s[i] > '9' || s[i] < '0' {
            return false
        }
    }
    
    return true
}

func getContent(log string) string {
    i := strings.Index(log, " ")
    return log[i+1:]
}

func getID(s string) string {
    i := strings.Index(s, " ")
    return s[:i]
}



/**
 * @param logs: the logs
 * @return: the log after sorting
 */
 import (
     "strings"
     "sort"
     "unicode"
)

func logSort (logs []string) []string {
    // Write your code here
    if len(logs) <= 1 {
        return logs
    }
    less := func(i, j int) bool {
        si := strings.SplitN(logs[i], " ", 2)
        sj := strings.SplitN(logs[j], " ", 2)
        idi, ci := si[0], si[1]
        idj, cj := sj[0], sj[1]
        iIsNumber, jIsNumber := number(ci), number(cj)
        if iIsNumber && jIsNumber {
            return i < j
        }
        if jIsNumber {
            return true
        }
        if iIsNumber {
            return false
        }
        if ci == cj {
            return strings.Compare(idi, idj) != 1
        }
        return strings.Compare(ci, cj) != 1
    }
    sort.SliceStable(logs, less)
    return logs
}

func number(s string) bool {
    splits := strings.Split(s, " ")
    for _, s := range splits {
        rs := []rune(s)
        for _, r := range rs {
            if !unicode.IsDigit(r) {
                return false
            }
        }
    }
    return true
}



/**
 * @param logs: the logs
 * @return: the log after sorting
 */
 
import "unicode"
import "sort"
import "fmt"
import "strings"

type logString []string

func (s logString) Len() int {
    return len(s)
}
func (s logString) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s logString) Less(i, j int) bool {
    var id1 []byte
    var id2 []byte
    len1 := len(s[i])
    len2 := len(s[j])
    index1 := 0
    index2 := 0
    for ; index1 < len1; index1++ {
        if s[i][index1] != ' ' {
            id1 = append(id1, byte(s[i][index1]))
            continue
        } else if s[i][index1] == ' ' {
            index1++
            break
        }
    }
    for ; index2 < len2; index2++ {
        if s[j][index2] != ' ' {
            id2 = append(id2, byte(s[j][index2]))
            continue
        } else if s[j][index2] == ' ' {
            index2++
            break
        }
    }

    result := strings.Compare(s[i][index1:], s[j][index2:])
    if result == -1 {
        return true
    } else if result == 1 {
        return false
    }

    result = strings.Compare(string(id1), string(id2))
    if result == -1 {
        return true
    } else {
        return false
    }
}

func logSort (logs []string) []string {
    // Write your code here
    letterString := make([]string, 0)
    numberString := make([]string, 0)
    for _, log := range logs {
        findText := false
        for _, letter := range log {
            if findText == false && !unicode.IsSpace(letter) {
                continue
            } else if findText == false && unicode.IsSpace(letter) {
                findText = true
                continue
            }
            if (unicode.IsDigit(letter)) {
                numberString = append(numberString, log)
            } else {
                letterString = append(letterString, log)
            }
            break
        }
    }
    sort.Sort(logString(letterString))
    ret := append(letterString, numberString...)
    fmt.Println(letterString)
    fmt.Println(numberString)
    return ret
}
