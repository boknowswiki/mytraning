// hash, not ac but should correct.

/**
 * @param longUrl: 
 * @return: nothing
 */
var l2s map[string]string
var s2l map[string]string
var base62 string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
var id int = -1

func encode (longUrl string) string {
    // 
    if shortURL, ok := l2s[longUrl]; ok {
        return shortURL
    }
    id++
    shortURL := encodeBase62(id)
    l2s[longUrl] = shortURL
    s2l[shortURL] = longUrl

    return shortURL
}

func encodeBase62(id int) string {
    ret := ""

    for id > 0 {
        ret = string(base62[id%62])+ret
        id /= 62
    }

    for len(ret) < 6 {
        ret = "0" + ret
    }

    return ret
}
