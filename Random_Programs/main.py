from getpass import getpass
def add_password(credentials):
     website=input("Enter the website name:")
     username=input("Enter the username:")
     password=getpass("Enter the password:")
     
    #  print("Website:",website)
    #  print("Username:",username)
     credential={
        "website":website,
        "username":username,
        "password":password
     }
     credentials.append(credential)
     print("\nPassword added successfully")




def main():
    credentials=[]
        
    while True:   
        print("================================")
        print("       PASSWORD MANAGER")
        print("================================")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            print("Add Password is selected")
            add_password(credentials)

        elif choice=="2":
            print("View Password is selected")
            print(credentials)

        elif choice=="3":
            print("Goodbye!!")
            break

        else:
            print("invalid choice")



if __name__=="__main__":
    main()
