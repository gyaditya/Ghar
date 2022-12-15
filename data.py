#Data Management by Adi
import json
import helper


#Load book data from JSON file
file = open("book_data.json", "r")
dataStr = file.read()
file.close()
books = json.loads(dataStr)

#Load Favourites from JSON file
file2 = open("fav.json", "r")
dataStr2 = file2.read()
file2.close()
favs = json.loads(dataStr2)

#Load User Information From JSON file
file3 = open("userinformation.json", "r")
dataStr3 = file3.read()
file3.close()
userinfo = json.loads(dataStr3)


#Make functions For all of the Options

#Option 1
def opt1():
        for i in range(len(books)):
            print(books[i]["title"], ",",
            books[i]["author"], "," ,
            books[i]["isbn"], "," ,
            books[i]["genre"])


#Option 2
def opt2():
        userin = input("Enter the Genre of your book:\n").lower()
        for i in range(len(books)):
            if userin == books[i]["genre"]:
                print(books[i]["title"], ",",
                books[i]["author"], "," ,
                books[i]["isbn"], "," ,
                books[i]["genre"])
                return
        print("None found")
        return


#Option 3
def opt3():
        userin = input("What is the data you want to sort by:\n").lower()
        if userin == "title" or "author" or "isbn" or "genre":
            helper.bubbleSort(books, userin)
            for i in range(len(books)):
                print(books[i]["title"], ",",
                books[i]["author"], "," ,
                books[i]["isbn"], "," ,
                books[i]["genre"])


#Option 4
def opt4():
        userin = input("What Is the name of the book you want to favouriate:\n").upper()
        for i in range(len(books)):
            if userin == books[i]["title"].upper():
                favs.append(books[i])
                print("Book Added")
                return
        print("Book was not found")
        return


#Option 5
def opt5():
        userin = input("Please enter The title of The book you want to Remove:\n").upper()
        for i in range(len(favs)):
            if userin == favs[i]["title"].upper():
                favs.pop(i)
                print("Book removed")
                return
        print("Book was not found")
        return

            
#Option 6
def opt6():
        for i in range(len(favs)):
            print(favs[i]["title"], ",",
            favs[i]["author"], "," ,
            favs[i]["isbn"], "," ,
            favs[i]["genre"])


#Write to JSON
def writejson():
        json_str = json.dumps(favs)
        with open("fav.json", "w") as f:
            f.write(json_str)

#Loops
userlogin = True
ProgramLoop = False

# User Login and Create Account

while userlogin:

    # Print the options
    print("Enter 'L' to log in:")
    print("Enter 'S' to sign up:")
    print("Enter 'E' to exit:")

    # Get the user's choice
    choice = input("Please Enter Your choice:\n").lower()

    # Log In
    if choice == "l":
        # Get the user information
        username = input("Enter your username:")
        password = input("Enter your password:")

        for i in range(len(userinfo)):
            if userinfo[i]["username"] == username and userinfo[i]["password"] == password:
                print("Login successful!")
                ProgramLoop = True
                userlogin = False
                break
            else:
            # In case user information not found
                print("Incorrect username or password.")

    # Signup
    elif choice == "s":
        username = input("Create a username:")
        password = input("Enter your password:")

        # If the username is not already in the users dictionary, add it
        for i in range(len(userinfo)):
            if userinfo[i]["username"] == username:
                print("Account Already exists")
                break
        else:
            userinfo.append({"username": username, "password": password, "favour":[]})
            print("Sign up successful!")
            ProgramLoop = True
            userlogin = False

    # Exit the loop
    elif choice == "e":
        # Set the userlogin variable to False to exit the loop
        userlogin = False

    # Invalid input
    else:
        print("Please enter a valid input")


# Upload to JSON
with open("userinformation.json", "w") as f:
    json.dump(userinfo, f)


#Start Looping For the Program
while ProgramLoop:

  #Options To pick From
    print("OPTION 1: Display all of the data")
    print("OPTION 2: Display some of the data")
    print("OPTION 3: Sort the data")
    print("OPTION 4: Select data to add to a favourites list / shopping cart")
    print("OPTION 5: Remove data from favourites list / shopping cart")
    print("OPTION 6: Display favourites list / shopping cart")
    print("OPTION 7: Exit")

    #Input From The user
    userInput = input("Pick your Option:")

    #Option 1
    if(userInput == "1"):
        opt1()

    #Option 2
    elif(userInput == "2"):
        opt2()

    #Option 3
    elif(userInput == "3"):
        opt3()

    #Option 4
    elif(userInput == "4"):
        opt4()

    #Option 5
    elif(userInput == "5"):
        opt5()

    #Option 6
    elif(userInput == "6"):
        opt6()

    #Option 7
    elif(userInput == "7"):
        writejson()
        break