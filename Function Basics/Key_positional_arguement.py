#key positional arguement it is like with key the arguement will be sent 

def Test(**kwargs):
    for key,value in kwargs.items():
        print(f"Key:{key} Value:{value}")
        
        
Test(Name = "Bhuvan Shetty", Age = "22")