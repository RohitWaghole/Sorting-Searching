# COUNT SORT 

'''
TIME COMPLEXITY
Best	O(n+k)
Worst	O(n+k)
Average	O(n+k)

SPACE COMPLEXITY
O(MAX ELEMENT OF ARRAY)
'''

arr = [3,2,4,3,5,6,3,3,5,4,3,2,1,3,5,4,3,2,2,5,5,6,6]

mx = max(arr)
frequency = [0]*(mx+1)
n = len(arr)

for i in arr:
    frequency[i] += 1

result = [0]*n

for i in range(1,mx+1):
    frequency[i] += frequency[i-1]
    

for i in range(n-1,-1,-1):
    frequency[arr[i]] -= 1
    result[frequency[arr[i]]] = arr[i]
    
for i in range(n):
    arr[i] = result[i]
    
print(arr)
