# This program is designed to ensure that the user creates a secure password within
# certain parameters.

# We can use booleans and any functions to analyze the password.
# We can then inform the user if the password is valid or not.


while True:
    p = input("Please create a password.\n\
It must be at least 6 characters long and no more than 20.\n\
It must also include at least 1 letter and 1 number.\n\
It cannot contain spaces. You may use an underscore instead.\n")

    pass_len = (6 <= len(p) <= 20)
    
    pass_letter = any(char.isalpha() for char in p)

    pass_num =  any(char.isdigit() for char in p)

    pass_space = p == p.strip()
    
    if pass_len == True and pass_letter == True and pass_num == True and pass_space == True:
        print("Your password is valid.")
    else:
        print(pass_len)
        print(pass_letter)
        print(pass_num)
        print(pass_space)
        print("Your password is invalid. Try again.")
        continue
    break
