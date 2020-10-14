/**
 * @param pid: the process id
 * @param ppid: the parent process id
 * @param kill: a PID you want to kill
 * @return: a list of PIDs of processes that will be killed in the end
 */
 
//import "fmt"
import "sort"

func killProcess (pid []int, ppid []int, kill int) []int {
    // Write your code here
    ppidToPid := make(map[int][]int)
    
    for i, pp := range ppid {
        //p, _ := ppidToPid[pp]
        //if !ok {
        //    p = make([]int, 0)
        //}
        ppidToPid[pp] = append(ppidToPid[pp], pid[i])
    }
    
    //fmt.Println(ppidToPid)
    
    ret := []int{}
    
    q := make([]int, 0)
    q = append(q, kill)
    
    for len(q) != 0 {
        //fmt.Println(q)
        p := q[0]
        q = q[1:len(q)]
        ret = append(ret, p)
        for _, pd := range ppidToPid[p] {
            q = append(q, pd)
        }
    }
    
    sort.IntSlice(ret).Sort()
    return ret
}
