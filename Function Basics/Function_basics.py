#A function is a block of code that performs specific task

#here a simple function will be written to add two numbers 

def add(a,b):
    return(a+b)

a = int(input("Enter the number1 "))
b = int(input("Enter the number2 "))
result = add(a,b)

print(result)


#-- now will give a default paramter --

def greeting(name = "guest"):   #This is a default paramter
    print(f"Hello {name}. How are you doing? ")

greeting("Bhuvan")# Here if we give value it willl be printed
greeting()# Else the default value will be printed


'''
Output:

PS D:\Gen AI -Full> & "d:/Gen AI -Full/venv/python.exe" "d:/Gen AI -Full/function.py"
Enter the number1 56
Enter the number2 54
110
Hello Bhuvan. How are you doing?
Hello guest. How are you doing?  '''
