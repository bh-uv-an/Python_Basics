#Dictionary basics 
print("Hello world ")

#creating dictionary using method 
dictry = dict()

#Creating dictionary
empty_dictionary = {}

#Creatind dictionary using function
New_dictionary = {}

#adding values to the dictionary
empty_dictionary = {"name":"Bhuvan Shetty", "Age":"22", "Sex":"Male"}
print("\nDictionary = ",empty_dictionary)

#Dictionary will not take values with same key 
#acessing dictionary with same elements 
print("\nAcessing elemnt using key = ",empty_dictionary["name"])

#acessing values using get method 
print("\nUsing get method = ",empty_dictionary.get("age"))  # it gives none as there is no key 
print("Using get method = ",empty_dictionary.get("Age"))

#If the element is not specified and if we want o get the default value then it can be done 
print(empty_dictionary.get("\nDoggy","\nSorry! not available "))

#modifying dictionary elements 
#dictionary are mutable which can be updated and then deleted 
empty_dictionary["Age"] = 23
print(empty_dictionary)
empty_dictionary["Fingers"] = 10
print(empty_dictionary)

#delete the key in dictionary
del empty_dictionary["Fingers"]
print("\nAfter deletion ",empty_dictionary)

#Dictionary method to get keys 
keys = empty_dictionary.keys()
print("\nKeys = ",keys)

#dictionary method to get values 
values = empty_dictionary.values()
print("\nValues = ",values)

#printing items in dictionary 
items = empty_dictionary.items()
print("\nItems = ",items)

#copy
copy = empty_dictionary
print("\nCopy = ",copy)

#Shallow copy
# this is basically just like ,the pointer here the memeory adress will be sent
# as reference to th new variable
copy_empty_dictionary = empty_dictionary.copy()
print("\ncopy_empty_dictionary = ",copy_empty_dictionary)


#iterating over dictionaries 
#here we can use for loop on keys values items
print("\nIterating through keys of dictionary")
for keys in empty_dictionary.keys():
    print("Keys = ",keys)
    
print("\n")
for values in empty_dictionary.values():
    print("Values = ",values)
    
print("\n")
for items in empty_dictionary.items():
    print("Items = ",items)


Output: 
'''
Hello world 

Dictionary =  {'name': 'Bhuvan Shetty', 'Age': '22', 'Sex': 'Male'}

Acessing elemnt using key =  Bhuvan Shetty

Using get method =  None
Using get method =  22

Sorry! not available
{'name': 'Bhuvan Shetty', 'Age': 23, 'Sex': 'Male'}
{'name': 'Bhuvan Shetty', 'Age': 23, 'Sex': 'Male', 'Fingers': 10}

After deletion  {'name': 'Bhuvan Shetty', 'Age': 23, 'Sex': 'Male'}

Keys =  dict_keys(['name', 'Age', 'Sex'])

Values =  dict_values(['Bhuvan Shetty', 23, 'Male'])

Items =  dict_items([('name', 'Bhuvan Shetty'), ('Age', 23), ('Sex', 'Male')])

Copy =  {'name': 'Bhuvan Shetty', 'Age': 23, 'Sex': 'Male'}

copy_empty_dictionary =  {'name': 'Bhuvan Shetty', 'Age': 23, 'Sex': 'Male'}

Iterating through keys of dictionary
Keys =  name
Keys =  Age
Keys =  Sex


Values =  Bhuvan Shetty
Values =  23
Values =  Male


Items =  ('name', 'Bhuvan Shetty')
Items =  ('Age', 23)
Items =  ('Sex', 'Male')
'''
