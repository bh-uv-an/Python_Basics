#map function basically it takes function name and itterables as a list and then does the work 
# It does the work that isbdefined in the function 

def add(a):
    return(a+a)

lst = [1,2,3,4,5,6]

temp = list(map(add,lst))

print(temp) #[2, 4, 6, 8, 10, 12]


# the same can be done using lambda function
temp2 = list(map(lambda x:x*x,lst))
print(temp2)    #[1, 4, 9, 16, 25, 36]

#Using two itterables to complete the operation 
lst2 = [7,8,9,10,11,12]

temp3 = list(map(lambda x,y:x+y,lst,lst2))
print(temp3)      #[8, 10, 12, 14, 16, 18]

lst3 = ["Bhuvan","Shubham","Aamna","Anvith"]
temp4 = list(map(str.upper,lst3))
print(temp4)    #['BHUVAN', 'SHUBHAM', 'AAMNA', 'ANVITH']



