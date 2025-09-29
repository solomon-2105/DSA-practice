def merge_sort(a,l,h):
    if l<h:
        mid=l+(h-l)//2
        merge_sort(a,l,mid)
        merge_sort(a,mid+1,h)
        merge(a,l,mid,h)

def merge(a,l,mid,h):
    n1=mid-l+1
    n2=h-mid
    b=[0]*n1
    s=[0]*n2
    for i in range(n1):
        b[i]=a[l+i]
    for j in range(n2):
        s[j]=a[mid+1+j]
    i,j=0,0
    k=l
    while i<n1 and j<n2:
        if b[i]<=s[j]:
            a[k]=b[i]
            i+=1
        else:
            a[k]=s[j]
            j+=1
        k+=1
    while i<n1:
        a[k]=b[i]
        i+=1
        k+=1
    while j<n2:
        a[k]=s[j]
        j+=1
        k+=1
a=list(map(int,input("enter the array elements : ").split()))
print("before sorting : ",end=" ")
print(*a)
l,h=0,len(a)-1
merge_sort(a,l,h)
print("after sorting : ",end=" ")
print(*a)