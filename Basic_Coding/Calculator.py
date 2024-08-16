a = []
i = 0
sum = 0
mul = 1
div = 0
sub = 0
while(True):
    num = int(input(f"Enter the number {i+1} "))
    a.append(num)
    str = input(print("TO STOP TYPE EXIT"))
    i += 1
    if(str == "EXIT" or str == "exit"):
        break
    
choice = int(input("Press \n1 - Add \n2 - Multiplication  \n3 - Subtraction"))

if(choice == 1):
    print("\nAddition operation is being performed")
    for i in range(len(a)):
        sum += a[i]
    
    print(sum)
        
elif(choice == 2):
    print("Multiplication operation is being performed ")
    for i in range(len(a)):
        mul *= a[i]
    
    print(mul)
            
elif(choice == 3):
    print("Subtraction is being performed")
    for i in range(len(a)):
        sub -= a[i]
        
    print(sub)
    
else:
    print("Invalid input")
