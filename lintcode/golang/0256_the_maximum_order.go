/**
 * @param onHand: the expiry days of m units of creamer already in stock
 * @param supplier: the expiry days of n units of creamer available for order
 * @param demand: the maximum units of creamer employees will uses daily
 * @return: the maximum units of creamer the manager can order without waste
 */
 
import "sort"

func stockLounge (onHand []int, supplier []int, demand int) int {
    // write your code here
    //m := len(onHand)
    n := len(supplier)
    
    sort.Ints(onHand)
    sort.Ints(supplier)
    
    for i, v := range onHand {
        if v < i/demand {
            return -1
        }
    }
    
    l := 0
    r := n
    
    for l + 1 < r {
        mid := (l+r)/2
        if valid(onHand, supplier, demand, mid) {
            l = mid
        } else {
            r = mid -1
        }
    }
    if valid(onHand, supplier, demand, r) {
        return r
    }
    return l
}

func valid(onHand []int, supplier []int, demand int, target int) bool {
    m := len(onHand)
    n := len(supplier)
    onIndex := 0
    supIndex := n-target
    
    for i := 0; i < m+target; i++ {
        if supIndex < n && (( onIndex < m && supplier[supIndex] < onHand[onIndex]) || onIndex == m) {
            if supplier[supIndex] < i/demand {
                return false
            }
            supIndex++
        } else {
            if onHand[onIndex] < i/demand {
                return false
            }
            onIndex++
        }
    }
    return true
}
