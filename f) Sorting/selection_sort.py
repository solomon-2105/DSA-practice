a=list(map(int,input("enter the array elements : ").split()))
print("before sorting : ",end=" ")
print(*a)
for i in range(len(a)-1):
    mini=i
    for j in range(i+1,len(a)):
        if a[j]<a[mini]:
            mini=j
    a[i],a[mini]=a[mini],a[i]
print("after sorting : ",end=" ")
print(*a)