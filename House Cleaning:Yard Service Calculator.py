# This program is designed to calculate the cost of house cleaning or yard maintenance
# for a business that provides these services.

# First, we must create functions to calculate the cost of the service requested.
# Here, we must check if the user input the correct type of value for each of their responses.

def num_check(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    return True

# Now we can ask the user for the other required inputs and check if they are valid.
def cln_service(num_rooms, num_baths, num_beds, num_windows, clean_type, senior):                       
    if 1 <= num_rooms <= 4:
        subtotal = 1 + (num_rooms * 2.50) + (num_baths * 7.50) + (num_beds * 3) + (num_windows * 15)
    elif 5 <= num_rooms <= 14:
        subtotal = 20 + (num_rooms * 2.75) + (num_baths * 10) + (num_beds * 5) + (num_windows * 18)
    elif 15 <= num_rooms:
        subtotal = 50 + (num_rooms * 3.15) + (num_baths * 12) + (num_beds * 7.50) + (num_windows * 20)
    if clean_type.lower() in ["deep", "deep clean", "d"]:
        total_bill = subtotal + (10 * num_rooms)
    elif clean_type.lower() in ["light", "light clean", "l"]:
        total_bill = subtotal
    if senior.lower() in ["yes", "y"]:
        estimate = (total_bill * .9)  
    elif senior.lower() in ["no", "n"]:
        estimate = total_bill
    return estimate

def yard_service(mow, edge, prune, senior):                       
    if 1 <= mow <= 1500:
        subtotal = 10 + (mow * .0018) + (edge * 2.50) + (prune * 8)
    elif 1501 <= mow <= 43559:
        subtotal = 40 + (mow * .0019) + (edge * 3.75) + (prune * 8) 
    elif 43560 <= mow:
        subtotal = 100 + (mow * .00225) + (edge* 6) + (prune * 8)
    if senior.lower() in ["yes", "y"]:
        total_bill = (subtotal * .9)  
    elif senior.lower() in ["no", "n"]:
        total_bill = subtotal
    return total_bill

def house_cln():

    print("\nThank you for choosing our house cleaning service.\nPlease answer the following questions about your home.\n")

    while True:
        num_rooms = input("How big is your home? (How many rooms does your house have?)\n")
        if num_check(num_rooms):
           num_rooms = float(num_rooms)
           if num_rooms >= 0:
               break
           else:
                print("\nPlease do not input negative numbers. Try again.\n")
        else:
            print("\nPlease type a number for the number of rooms. Try again.\n")

    while True:
        num_baths = input("How many bathrooms do you need cleaned?\n")
        if num_check(num_baths):
           num_baths = float(num_baths)
           if num_baths >= 0:
               break
           else:
                print("\nPlease do not input negative numbers. Try again.\n")
        else:
            print("\nPlease type a number for the number of bathrooms. Try again.\n")

    while True:
        num_beds = input("How many beds do you want made with new sheets?\n")
        if num_check(num_beds):
           num_beds = float(num_beds)
           if num_beds >= 0:
               break
           else:
                print("\nPlease do not input negative numbers. Try again.\n")
        else:
            print("\nPlease type a number for the number of beds to be made. Try again.\n")

    while True:
        num_windows = input("How many windows do you need cleaned?\n")
        if num_check(num_windows):
           num_windows = float(num_windows)
           if num_windows >= 0:
               break
           else:
                print("\nPlease do not input negative numbers. Try again.\n")
        else:
            print("\nPlease type a number for the number of windows to be cleaned. Try again.\n")
            
    while True:
        clean_type = input("Would you like a deep or light cleaning of your rooms?\n")

        if clean_type.lower() in ["deep", "deep clean", "d"]:
            answer = True
            break
        elif clean_type.lower() in ["light clean", "light", "l"]:
            answer = True
            break
        else:
            print("\nPlease indicate if you want a deep or light cleaning for your rooms.\n")
            
    while True:
        senior = input("Are you a senior citizen above the age of 60?\n")

        if senior.lower() in ["yes", "y"]:
            answer = True
            break
        elif senior.lower() in ["no", "n"]:
            answer = True
            break
        else:
            print("\nIndicate your answer as yes or no only. Please try again.\n")
            
    a = cln_service(num_rooms, num_baths, num_beds, num_windows, clean_type, senior)
    print("A total estimate for this job is $", "{0:.2f}".format(a), ".\n", sep="")
    return a
    
# Now we can charge different amounts based on how big the client's house is.



    #a = cln_service(num_rooms, num_baths, num_beds, num_windows, clean_type)
    
# Now we can print the results to show the client the quotation for our
# expert cleaning services.

    #return a
    #print("A total estimate for this job is $", "{0:.2f}".format(a), ".\n", sep="")

def yard_main():
    print("\nThank you for choosing our yard/lawn care service.\nPlease answer the following questions about your yard.\n")
    
# Here, we must check if the user's inputs are valid.

    while True:
        mow = input("How big is your yard/lawn in square feet (1 acre = 43,560 square feet)?\n")
        if num_check(mow):
            mow = float(mow)
            if mow >= 0:
                break
            else:
                print("\nPlease do not input negative numbers. Try again.\n")
        else:
            print("Please type a number for how large the yard is. Try again.\n")

    while True:            
        edge = input("How many edges do you want to be trimmed?\n")
        if num_check(edge):
            edge = float(edge)
            if edge >= 0:
                break
            else:
                print("\nPlease do not input negative numbers. Try again.\n")
        else:
            print("Please type a number for how large the yard is. Try again.\n")

    while True:
        prune = input("How many bushes and/or trees do you want to be pruned?\n")
        if num_check(prune):
            prune = float(prune)
            if prune >= 0:
                break
            else:
                print("\nPlease do not input negative numbers. Try again.\n")
        else:
            print("Please type a number for how large the yard is. Try again.\n")
            
    while True:
        senior = input("Are you a senior citizen above the age of 60?\n")

        if senior.lower() in ["yes", "y"]:
            answer = True
            break
        elif senior.lower() in ["no", "n"]:
            answer = True
            break
        else:
            print("\nIndicate your answer as yes or no only. Please try again.\n")

    b = yard_service(mow, edge, prune, senior)
    print("A total estimate for this job is $", "{0:.2f}".format(b), ".\n", sep="")
    return b

# Now we can charge different amounts based on how big the client's yard is.



   # b = yard_service(mow, edge, prune)
    
# Now we can print the results to show the client the quotation for our
# expert lawn care services.

    #return b
    #print("A total estimate for this job is $", "{0:.2f}".format(b), ".\n", sep="")
    
# Now that the functions for the services are defined, we can call them and ask the user
# which service they are inquiring about.
    
while True:
    service = input("Would you like to schedule house cleaning or yard maintenance service today?\nYou may also choose both.\n")
    if service.lower() in ["house cleaning", "house", "cleaning", "h", "c"]:
        answer = True
        print("You have selected house cleaning.\n")
        house_cln()
        break
    elif service.lower() in ["yard maintenance", "yard", "maintenance", "lawn", "y"]:
        answer = True
        print("You have selected yard maintenance.\n")
        yard_main()
        break
    elif service.lower() in ["both", "b"]:
        answer = True
        print("You have selected both services.\n")
        c = house_cln() + yard_main()
        print("A total estimate for both jobs is $", "{0:.2f}".format(c), ".\n", sep="")
        break
    else:
        print("\nThat service is not available. Please try again.\n") 
