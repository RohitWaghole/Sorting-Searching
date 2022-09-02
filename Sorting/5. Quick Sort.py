# QUICK SORT

def partition(a,lo,hi):
    
    i = lo-1
    pivot = a[hi]
    
    for j in range(lo,hi):
        if a[j] < pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    i+=1
    a[i],a[hi] = a[hi],a[i]
    return i
    
    
def QuickSort(a,lo,hi):
    if lo<hi:
        pivotLocation = partition(a,lo,hi)
        QuickSort(a, lo, pivotLocation-1)
        QuickSort(a, pivotLocation+1, hi)
        
        
        
a = [5,8,7,9,0,6,4,1,2,3]

QuickSort(a, 0, len(a)-1)
print(a)
