/**
 * @param stores: The location of each store.
 * @param houses: The location of each house.
 * @return: The location of the nearest store to each house.
 */
 
import "sort"
//import "fmt"

func findNearestStore (stores []int, houses []int) []int {
    // 
    sort.Ints(stores)
    ret := make([]int, len(houses))
    
    //fmt.Println(stores, ret)
    for i, h := range houses {
        ret[i] = getStore(stores, h)
        //fmt.Println(i, h, ret[i])
    }
    
    return ret
}

func getStore(stores []int, target int) int {
    l := 0
    r := len(stores)-1
    //fmt.Println(l, r, target)
    for l+1 < r {
        mid := (l+r)/2
        //fmt.Println(l, r, mid)
        if stores[mid] <= target {
            l = mid
        } else {
            r = mid
        }
    }
    
    //fmt.Println(l, r, target)
    if abs(stores[l]-target) <= abs(stores[r]-target) {
        //fmt.Println(l, r, target)
        return stores[l]
    }
    return stores[r]
}

func abs(a int) int {
    //fmt.Println(a)
    if a < 0 {
        return -a
    }
    return a
}
