# SELECTION SORT

a = [10290,15293,2412,324,23813,3234,29384,2585,219,83295,648746,233]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
