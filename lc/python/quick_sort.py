#!/usr/bin/python -t

def partition(nums, start, end):
    pivot = nums[end] #could be pivot = nums[start] as well
    i = start - 1

    for j in range(start, end):
        if nums[j] <= pivot:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[end] = nums[end], nums[i+1]

    return i+1


def quick_sort(nums, start, end):
    if start < end:
        pivot = partition(nums, start, end)

        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)
    

# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i]) 

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is:")  
    printList(arr) 
    quick_sort(arr, 0, len(arr)-1) 
    print("Sorted array is:") 
    printList(arr) 
  
