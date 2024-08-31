#Filter function is used to filter out the eelemnts based on the condition 

lst = [1,2,3,4,5,6,7,8,9]

def is_even(num):
    if num%2 == 0:
        return True
    
temp1 = list(filter(is_even,lst))

print(temp1)    #[2, 4, 6, 8]


#to print numbers greater than 5

def greater_then(number):
    if(number>=5):
        return True

lst2 = [5,6,7,8,9,10,11,12,13,14,15]

lst3 = list(filter(greater_then,lst2))

print(lst3)     #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# applying filter with multiple condition

lst4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

temp2 = list(filter(lambda x:x>5 and  x%2 == 0,lst4))

print(temp2)