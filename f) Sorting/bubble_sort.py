a=list(map(int,input("enter the array elements : ").split()))
print("before sorting : ",end=" ")
print(*a)
i=0
while i<len(a):
    j=0
    while j<len(a)-i-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    i+=1
print("after sorting : ",end=" ")
print(*a)