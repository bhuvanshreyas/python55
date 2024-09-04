def linearsearch(a,key):
    n=len(a)
    for i in range(n):
        if a[i]==key:
            for i in range(n):
                if a[i]==key:
            return i;
    return -1
a=[1,2,3,4,5,66,7] 
print("the array list",a)
k=int(input("enter the element:"))
i=linearsearch(a,k) 
if i == -1:
    print("unsucessful")
else:
    print("sucessful",i+1)
  