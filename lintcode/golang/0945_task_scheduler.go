/**
 * @param tasks: the given char array representing tasks CPU need to do
 * @param n: the non-negative cooling interval
 * @return: the least number of intervals the CPU will take to finish all the given tasks
 */
import "container/heap"
import "fmt"

func leastInterval (tasks string, n int) int {
    h := new(ItemHeap)
    m := make(map[byte]int)
    count := 0
    
    for _, task := range tasks {
        m[byte(task)]++
    }
    
    for task, occur := range m {
        heap.Push(h, &Item{ task, occur })
    }
    
    //fmt.Printf("h len %v", h.Len())
    
    for {
        k := n + 1
        items := make([]*Item, 0)
        
        for k > 0 && h.Len() > 0 {
            item := heap.Pop(h).(*Item)
            item.occur--
            items = append(items, item)
            count++
            k--
        }
        
        //fmt.Printf("items %#v\n", items)
        
        for _, item := range items {
            if item.occur > 0 {
                heap.Push(h, item)
            }
        }
        
        if h.Len() == 0 {
            break
        }
        
        count += k
    }
    
    
    
    return count
}

type Item struct {
    task byte
    occur int
}

type ItemHeap []*Item

func (h ItemHeap) Len() int { return len(h) }
func (h ItemHeap) Less(i, j int) bool { return h[i].occur > h[j].occur }
func (h ItemHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *ItemHeap) Push(x interface{}) { *h = append(*h, x.(*Item)) }

func (h *ItemHeap) Pop() interface{} {
    ele := (*h)[len(*h)-1]
    *h = (*h)[:len(*h)-1]
    return ele
}
