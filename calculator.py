a=int(input("enter first number:"))
b=int(input("enter second number:"))
choice=0
while choice<=6:
    print("---CALCULATOR MENU---")
    print("1-addition")
    print("2-substraction")
    print("3-multiplication")
    print("4-division")
    print("5-remainder")
    print("6-exit")
    choice=int(input("select the operation(1-6) :"))

    if choice==1:
      print("the sum is :",a+b)
    elif choice==2:
      print("the substraction is :",a-b)
    elif choice==3:
      print("the multiplication is :",a*b)
    elif choice==4:
      print("the division is :",a/b)
    elif choice==5:
      print("the remainder is :",a%b)
    elif choice==6:
       break
    else:
      print("invalid operation selected !")