import re 

pattern = r'\d+'
text = "Hi, my name is bhuvan 1234"
match = re.search(pattern,text)

print(match.group())

'''
Output:
PS D:\Gen AI -Full> & "d:/Gen AI -Full/venv/python.exe" "d:/Gen AI -Full/Regular_expression.py"
1234
'''