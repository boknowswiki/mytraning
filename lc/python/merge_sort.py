#!/usr/bin/python -t

def merge(l, r):
    n_l = len(l)
    n_r = len(r)

    ret = []

    i = 0
    j = 0

    while i < n_l and j < n_r:
        if l[i] < r[j]:
            ret.append(l[i])
            i = i + 1
        else:
            ret.append(r[j])
            j = j + 1

    while i < n_l:
        ret.append(l[i])
        i = i + 1

    while j < n_r:
        ret.append(r[j])
        j = j + 1

    return ret

    

def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    #l = 0
    #r = n - 1
    #mid = l + (r-l)/2
    mid = n/2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i]) 

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is:")  
    printList(arr) 
    new_arr = merge_sort(arr) 
    print("Sorted array is:") 
    printList(new_arr) 
  
