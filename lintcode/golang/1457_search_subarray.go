/**
 * @param arr: The array 
 * @param k: the sum 
 * @return: The length of the array
 */

//import "fmt"

func searchSubarray (arr []int, k int) int {
    // Write your code here
    n := len(arr)
    if n == 0 {
        return 0
    }

    preSum := make([]int, n+1)

    for i := 0; i < n; i++ {
        preSum[i+1] = preSum[i] + arr[i]
    }

    //fmt.Println(preSum)

    d := make(map[int]int)

    for i:=n; i >= 0; i-- {
        d[preSum[i]] = i
    }

    //fmt.Println(d)

    for i := 0; i < n+1; i++ {
        v, ok := d[preSum[i]-k]
        if ok && i > v {
            return i-v
        }
    }

    return -1
}

