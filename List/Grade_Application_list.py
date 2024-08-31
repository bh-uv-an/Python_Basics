#Inputting grade
n = int(input("Enter the subjects of students "))

#initializing the list 
lst = []

#itterating throug the inputted students 
for i in range(1,n+1):
    print(f"Enter the marks for Subject {i}")
    ele = int(input())
    lst.append(ele)
    
#printing all the marks of the students 
print("\n",lst)

#Finding the Sum in the list
sum = 0
for i in lst:
    sum = sum + i 
print("\nSum = ",sum)
    
# finding the averaage in the list 
avg = sum/n
print(f"\nAvg = ",avg)

#FInding thw hieghest marks and lowest marks in the lst
print("\nHiehest marks in list ",max(lst))
print("Lowest marks in the list ",min(lst))