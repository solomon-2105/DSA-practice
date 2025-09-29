def merge_sort(a,l,h):
    if l<h:
        mid=l+(h-l)//2
        merge_sort(a,l,mid)
        merge_sort(a,mid+1,h)
        merge(a,l,mid,h)

def merge(a,l,mid,h):
    i,j=l,mid+1
    while i<=mid and j<=h:
        if a[i]<=a[j]:
            i+=1
        else:
            temp=a[j]
            ind=j
            while ind>i:
                a[ind]=a[ind-1]
                ind-=1
            a[i]=temp
            i+=1
            mid+=1
            j+=1
a=list(map(int,input("enter the array elements : ").split()))
print("before sorting : ",end=" ")
print(*a)
l,h=0,len(a)-1
merge_sort(a,l,h)
print("after sorting : ",end=" ")
print(*a)