username = input("What is your username: \n")
allowed_users = ["Seyi","John","Grant"]
allowed_passwords = ["passwordSeyi","passwordJohn","passwordGrant"]

if(username in allowed_users):
    password = input("Enter password: \n")
    userId = allowed_users.index(username)

    if(password == allowed_passwords[userId]):
        print("Welcome %s" % username)
        print("These are the available options: ")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")

        selectedOption = int(input("Please select an option: \n"))

        if selectedOption == 1:
            amount = input("Enter amount: ")
            if int(amount) <= 4999:
                print("Click the red button")
            if int(amount) == 5000 < 9999:
                print("Click the green button")
            if int(amount) >= 10000:
                print("Click the blue button ")

        elif(selectedOption == 2):
            amount = input("How much are you depoiting: \n")
            if int(amount) <= 5000:
                print("Click the red button")
            if int(amount) > 5000 < 10000:
                print("Click the green button")
            if int(amount) >= 10000:
                print("Please go into the banking hall to make your deposit")

        elif(selectedOption == 3):
            print("What will you like to do?")
            print("1. Send an Email")
            print("2. Call us")
            print("3. Schedule a meeting with an agent")
            
            complaints = int(input("Select an option above: \n"))
            if int(complaints) == 1:
                print("Send your email to info@bankphb.com")
            if int(complaints) == 2:
                print("Call this number +2348146384065")
            if int(complaints) == 3:
                print("Sync your app calender to schedule a date. Thank You for banking with us. ")


        else:
            print("Invalid option selected, please try again.")

    else:
        print("Password incorrect, please try again")

else:
    print("Name not found")