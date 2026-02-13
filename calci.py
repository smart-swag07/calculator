num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

operator=input("Enter operator (+, -, *, /): ")

if operator=='+':
    res=num1+num2  
elif operator=='-':
    res=num1-num2
    
elif operator=='*':
    res=num1*num2
    
elif operator=='/':
     res=num1/num2

print(f"Result of {num1}{operator}{num2} : {res:.2f}")