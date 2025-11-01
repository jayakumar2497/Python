name=str(input("Enter Your Name :"))
age=int(input("Enter Your Age"))

if age>=18:
  expe=int(input("Enter Your Experience"))
  if expe > 0:
          print("you are eligible")
  else:
          print("sorry not eligible")
else:
  print("Sorry Age Must Be 18")  
    