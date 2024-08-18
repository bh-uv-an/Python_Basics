lst = []

for i in range(1,10):
    lst.append(i)
    
print(lst)

print("Adding element to the specific index")

lst.insert(9,10)        #list.insert(index, element)

print("Updated Element",lst)

print("To remove the last element pop is used")

print(lst.pop())

print(lst)

print("To find index ")

print("Index of the element 3 is ",lst.index(3))

print("To count the number of specific elements in the list ")

lst.append(5)
print(lst)

print(lst.count(5))

print("TO sort elements")
lst.sort()
print(lst)

print("TO reverse elements")
lst.reverse()
print(lst)

print("TO clear elemets")
lst.clear()
print(lst)
