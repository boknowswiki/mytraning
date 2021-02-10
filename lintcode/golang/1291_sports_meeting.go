/**
 * @param Events: the start and end time
 * @return: if there has a solution return 1, otherwise return -1.
 */
func CheerAll (Events [][]int) int {
    // write your code here
        arr:=make([][]int,0)
    for i:=0;i<len(Events);i++{
        start:=(Events[i][1]-Events[i][0])/2+1
        arr=append(arr,[]int{Events[i][0],start,Events[i][1]})
        insertsort(arr)
    }
    // for i:=len(arr)-1;i>1;i--{
    //     if arr[i-1][2]>arr[i][1]{
    //         return -1
    //     }
    // }
    t:=arr[0][0]
    for i:=0;i<len(arr);i++{
        if t<arr[i][0]{
            t=arr[i][0]
        }
        t+=arr[i][1]
        if t>arr[i][2]{
            return -1
        }
        
    }
    // if len(arr)>=2{
    //     if arr[0][2]-(arr[0][2]-arr[0][0]-1)/2>arr[1][1]{
    //         return -1
    //     }
    // }
    return 1
}

func insertsort(arr [][]int){
    tmp:=arr[len(arr)-1]
    for i:=len(arr)-2;i>=0;i--{
        if arr[i][2]-arr[i][1]>tmp[2]-tmp[1]{
            arr[i+1]=arr[i]
            if i==0{
                arr[i]=tmp
            }
        }else{
            arr[i+1]=tmp
            break
        }
    }
}
