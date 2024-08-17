list1 = [i for i in range(10)]
list2 = ["a","b","c","d","e","f","g","h","i","j"]

print(list1)
print(list2)

combined_list = [[i,j] for i in list1 for j in list2]

print(combined_list)