
// 初始假定给每个小孩都分一颗糖果, 即设定一个全1的 count 数组.
// 
// 然后我们开始修正这个数组:
// 
// 首先从左到右遍历, 如果发现一个小孩左边的小孩比自己的 rating 低, 那么把这个小孩的糖果数设为他左边的小孩 + 1
// 
// 这时我们分配的糖果已经满足了: 评分更高的小孩比他左边的小孩获得更多的糖果. 然后我们再从右往左遍历一次就可以了.
// 
// 但是这时还应该注意一点: 当一个小孩右边的小孩比自己的 rating 低时, 这个小孩的糖果可能已经比他右边的小孩多了, 而且可能多不止一个, 这时应该保留他的糖果数目不变.
// 
// 比如这组数据: [1, 2, 3, 4, 1], 初始 count 数组为 [1, 1, 1, 1, 1], 第一次遍历之后变成 [1, 2, 3, 4, 1], 第二次遍历不应该再改变这个数组了.


/**
 * @param ratings: Children's ratings
 * @return: the minimum candies you must give
 */
func candy (ratings []int) int {
    // write your code here
    ret := make([]int, len(ratings))
    
    for i := range(ret) {
        ret[i] = 1
    }
    
    for i := 1; i < len(ratings); i++ {
        if ratings[i] > ratings[i-1] {
            ret[i] = ret[i-1]+1
        }
    }
    
    for i := len(ratings)-2; i >= 0; i-- {
        if ratings[i] > ratings[i+1] && ret[i] <= ret[i+1] {
            ret[i] = ret[i+1]+1
        }
    }
    
    r := 0
    
    for i := range ret {
        r += ret[i]
    }
    
    return r
}


