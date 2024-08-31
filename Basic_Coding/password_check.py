def password_Check(password):
    if len(password)<5:
        return False
    
    if not any(letter.isdigit() for letter in password):
        return False
    
    if not any(letter.islower() for letter in password):
        return True
    
    if not any(letter.isupper() for letter in password):
        return False
    
    return True


password = input("Enter the string ")
print(password_Check(password))