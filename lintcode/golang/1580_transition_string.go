
/**
 * @param startString: a string
 * @param endString: a string
 * @return: if startString can be converted to endString
 */
func canTransfer (startString string, endString string) bool {
    // write your code here
    lenS := len(startString)
    lenE := len(endString)
    if lenS != lenE {
        return false
    }

    m := make(map[string]string)

    for i :=0; i < lenS; i++ {
        if val, ok := m[string(startString[i])]; ok {
            if val != string(endString[i]) {
                return false
            }
        } else {
            m[string(startString[i])] = string(endString[i])
        }
    }

    for _, v := range m {
        visited := make(map[string]bool)
        for val, ok := m[v]; ok; val, ok = m[v] {
            visited[v] = true
            last := v
            v = val
            if v == last {
                break
            }
            if _, found := visited[v]; found {
                return false
            }
        }
    }

    return true
}


/**
 * @param startString: a string
 * @param endString: a string
 * @return: if startString can be converted to endString
 */
func canTransfer (startString string, endString string) bool {
    // write your code here
    lenS := len(startString)
    lenE := len(endString)
    if lenS != lenE {
        return false
    }

    m := make(map[string]string)

    for i :=0; i < lenS; i++ {
        if val, ok := m[string(startString[i])]; ok {
            if val != string(endString[i]) {
                return false
            }
        } else {
            m[string(startString[i])] = string(endString[i])
        }
    }

    for _, v := range m {
        visited := make(map[string]bool)
        for {
            if val, ok := m[v]; ok {
                visited[v] = true
                last := v
                v = val
                if v == last {
                    break
                }
                if _, found := visited[v]; found {
                    return false
                }
            } else {
                break
            }
        }
    }

    return true
}

