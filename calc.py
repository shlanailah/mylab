user1=""
while user1!="=":
    num1=float(input("Enter a number: "))
    operator1=(input("Enter an operator (+,-,*,/): "))
    num2=float(input("Enter another number: "))
    count=user1+str(num1)+str(operator1)+str(num2)
    print(count)
    operator2=(input("Enter an operator (+,-,*,/): "))
    count+=operator2
    print(count)