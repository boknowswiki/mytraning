#!/usr/bin/python -t

def heapify(nums, end, start):
    max_val = start
    l = 2*start + 1
    r = 2*start + 2

    if l < end and nums[l] > nums[start]:
        max_val = l

    if r < end and nums[r] > nums[max_val]:
        max_val = r

    if max_val != start:
        nums[max_val], nums[start] = nums[start], nums[max_val]

        heapify(nums, end, max_val)


def heap_sort(nums):
    n = len(nums)

    #build max heap
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    

# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i]) 

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is:")  
    printList(arr) 
    heap_sort(arr) 
    print("Sorted array is:") 
    printList(arr) 
  
