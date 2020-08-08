func hIndex(citations []int) int {
    n := len(citations)
    l, r := 0, n - 1
    for l <= r {
        m := l + (r - l) / 2
        if citations[m] < n - m {
            l = m + 1
        } else {
            r = m - 1
        }
    }
    return n - l
}
