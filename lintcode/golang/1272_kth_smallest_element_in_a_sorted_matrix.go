func kthSmallest(matrix [][]int, k int) int {
    l:= matrix[0][0]
    r:= matrix[len(matrix)-1][len(matrix)-1]
    
    for l < r {
        mid := (l+r)/2
        if getCnt(matrix, mid) < k {
            l = mid+1
        } else {
            r = mid
        }
    }
    
    return l
}

func getCnt(matrix [][]int, target int) int {
    var cnt int
    row := 0
    col := len(matrix)-1
    
    for row < len(matrix) && col >= 0 {
        if matrix[row][col] <= target {
            row += 1
            cnt += col+1
        } else {
            col -= 1
        }
    }
    
    return cnt
}
