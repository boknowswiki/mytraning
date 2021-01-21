/**
 * @param nums: A list of integer which is 0, 1 or 2 
 * @return: nothing
 */
func sortColors (nums *[]int)  {
    // write your code here
    n := len(*nums)
    i := 0
    l := 0
    r := n-1
    
    for i <= r {
        if (*nums)[i] == 0 {
            (*nums)[i], (*nums)[l] = (*nums)[l], (*nums)[i]
            i++
            l++
        } else if (*nums)[i] == 1 {
            i++
        } else if (*nums)[i] == 2 {
            (*nums)[i], (*nums)[r] = (*nums)[r], (*nums)[i]
            r--
        }
    }
    
    return
}

