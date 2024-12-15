// time O(n)
// space O(n)

func reverseWords(s string) string {
    ret := ""

    for i := 0; i < len(s); i++ {
        if s[i] == ' ' {
            continue
        }

        j := i
        for j < len(s) && s[j] != ' ' {
            j++
        }

        if ret == "" {
            ret = s[i:j]
        } else {
            ret = s[i:j] + " " + ret
        }
        i = j
    }

    return ret
}
