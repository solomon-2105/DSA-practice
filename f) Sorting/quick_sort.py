def quick_sort(a,l,h):
    if l<h:
        p=partition(a,l,h)
        quick_sort(a,l,p-1)
        quick_sort(a,p+1,h)
def partition(a,l,h):
    pivot=a[l]
    i,j=l,h
    while i<j:
        while i<=h and a[i]<=pivot:
            i+=1
        while a[j]>pivot and j>=l:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j
a=list(map(int,input("enter the array elements : ").split()))
print("before sorting : ",end=" ")
print(*a)
l,h=0,len(a)-1
quick_sort(a,l,h)
print("after sorting : ",end=" ")
print(*a)