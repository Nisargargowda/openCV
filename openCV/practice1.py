lst =  []

n = int(input("Enter number of elements : "))
print("Enter array elements")
for i in range (0, n):
    ele = int(input())
    lst.append(ele)

print(lst)

largest = lst[0]
for j in range(0, n):
    if(lst[j]>largest):
        largest = lst[j]
print(largest)