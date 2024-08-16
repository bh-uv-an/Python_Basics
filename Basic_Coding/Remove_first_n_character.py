str = input("Enter the string ")
n = int(input("Enter the skip postion "))
# str = "bhuvan"
if n>len(str):
    print("Not possible")
else:
    print(str[n:])
    


'''
Output:
Enter the string pynative
Enter the skip postion 4
tive
'''