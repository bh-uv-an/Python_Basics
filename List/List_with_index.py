lst = []

for i in range(20):
    lst.append(i)
    
print(lst)

for index,elements in enumerate(lst):
    print(f"\n Index {index} \t Element {elements}")