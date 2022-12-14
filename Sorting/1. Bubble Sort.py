# BUBBLE SORT

'''
TIME COMPLEXITY
Best	-> O(n)
Worst	-> O(n^2)
Average	-> O(n^2)

SPACE COMPLEXITY
O(1)
'''

a = [10290,15293,2412,324,23813,3234,29384,2585,219,83295,648746,233]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)

####################################################################################################

a = [10290,15293,2412,324,23813,3234,29384,2585,219,83295,648746,233]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)

######################################################################################################

a = [10290,15293,2412,324,23813,3234,29384,2585,219,83295,648746,233]
for i in range(len(a)):
    flag = 1
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            flag = 0
    if flag:
        break
print(a)
