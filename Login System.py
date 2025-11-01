User="Jayakumar"
Passkey="Jay@2497K"
Username=str(input("Enter Your UserName:"))
if Username==User:
    print("Username is correct")
    password=input("Enter the Password")
    if password==Passkey:
       print("Suessfully Loged in")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")