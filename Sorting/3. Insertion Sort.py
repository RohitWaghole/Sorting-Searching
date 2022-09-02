# INSERTION SORT

'''
TIME COMPLEXITY
Best	-> O(n)
Worst	-> O(n2)
Average	-> O(n2)

SPACE COMPLEXITY
O(1)
'''

a = [10290,15293,2412,324,23813,3234,29384,2585,219,83295,648746,233]

for i in range(1,len(a)):
    
    temp = a[i]
    j = i-1
    
    while j>=0 and a[j]>temp:
        a[j+1] = a[j]
        j-=1
    a[j+1] = temp

print(a)
