/**
 * @param arr: the map
 * @return:  the smallest target that satisfies from the upper left corner (0, 0) to the lower right corner (n-1, n-1)
 */
//import "fmt"

func mapJump (arr [][]int) int {
    // Write your code here.
    m := len(arr)
    if m == 0 {
        return 0
    }
    //n := len(arr[0])
    l := 0
    r := 100000
    for l +1 < r {
        mid := l + (r-l)/2
        //fmt.Println(mid)
        if canJump(arr, mid) {
            r = mid
        } else {
            l = mid
        }
    }
    
    if canJump(arr, l) {
        return l
    }
    
    return r
}

func coverXY (val, n int) (int, int) {
    return val/n, val%n
}

func canJump(arr [][]int, target int) bool {
    q := make([]int, 0)
    q = append(q, 0)
    visit := make(map[int]bool)
    
    directions := []struct {
        dx int
        dy int
    }{{-1,0,},{0,-1},{0,1},{1,0}}
    
    for len(q) > 0 {
        x, y := coverXY(q[0], len(arr))
        q = q[1:]
        //fmt.Println(x, y, q)
        if (x == len(arr)-1) && (y == len(arr[0])-1) {
            //fmt.Println(x, y)
            return true
        }
        var cx, cy int
        for i := 0; i < 4; i++ {
            cx = x + directions[i].dx;
            cy = y + directions[i].dy;
        
            if valid(arr, cx, cy, arr[x][y], target, visit) {
                q = append(q, cx*len(arr)+cy)
                visit[cx*len(arr)+cy] = true
            }
        }
    }
    return false
}

func valid(arr [][]int, cx, cy, org, target int, visit map[int]bool) bool {
    if cx < 0 || cy < 0 || cx >= len(arr) || cy >= len(arr[0]) {
        return false
    }
    if _, ok := visit[cx*len(arr)+cy]; ok {
        return false
    }
    if abs(arr[cx][cy] - org) > target {
        return false
    }
    //fmt.Println(cx, cy, org, target)
    return true
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
