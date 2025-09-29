a=list(map(int,input("enter the array elements : ").split()))
print("before sorting : ",end=" ")
print(*a)

for i in range(len(a)):
    j=i
    while j>0 and a[j-1]>a[j]:
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
print("after sorting : ",end=" ")
print(*a)