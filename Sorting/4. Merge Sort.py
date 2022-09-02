# MERGE SORT

'''
TIME COMPLEXITY
Best	-> O(n*log n)
Worst	-> O(n*log n)
Average	-> O(n*log n)

SPACE COMPLEXITY
O(n)
'''

def merge(arr, start, mid, end):
    
    len1 = mid - start + 1
    len2 = end - mid
    
    first = [0]*len1
    second = [0]*len2
    
    mainArrayIndex = start
    for i in range(0,len1):
        first[i] = arr[mainArrayIndex]
        mainArrayIndex += 1
    
    mainArrayIndex = mid + 1
    for i in range(0,len2):
        second[i] = arr[mainArrayIndex]
        mainArrayIndex += 1
        
    index1 = 0
    index2 = 0
    mainArrayIndex = start
    
    while index1<len1 and index2<len2:
        if first[index1] <= second[index2]:
            arr[mainArrayIndex] = first[index1]
            index1 += 1
        else:
            arr[mainArrayIndex] = second[index2]
            index2 += 1
        mainArrayIndex += 1 
    
    while index1 < len1:
        arr[mainArrayIndex] = first[index1]
        mainArrayIndex += 1
        index1 += 1
    
    while index2 < len2:
        arr[mainArrayIndex] = second[index2]
        mainArrayIndex += 1
        index2 += 1
          
def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end)//2
        
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        
        merge(arr, start, mid, end)
        
arr = [2,34,4,32,6,3,21,56,37,7,5,9,34,0]
n = len(arr)
  
mergeSort(arr, 0, n-1)
print(arr)
            
