#positional arguement is like if we have series of elements as arguements then we go with positiona
# arguements 

def add(*args):
    sum = 0
    for elements in args:
        sum += elements
        
    return sum

a = int(input("Enter the number 1 "))
b = int(input("Enter the number 2 "))
print(add(a,b))