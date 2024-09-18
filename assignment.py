
def summation(a,b):
    print(a," + ",b, " = ",a+b)

def substraction(a,b):
    print(a," - ",b, " = ",a-b)

def division(a,b):
    try:
        print(a," / ",b," = ",a/b)
    except ZeroDivisionError:
        print("ERROR!! Wrong denominator. Denominator must not be eqaul to zero")

def multiplication(a,b):
    print(a,"*",b," = ",a*b )

def modulus(a,b):
    print(a,"%",b," = ",a%b )

print("Select operation: ""\n"
      "1.ADD""\n"
      "2.SUBTRACT""\n"
      "3.MULTIPLY""\n"
      "4.DIVIDE""\n"
      "5.MODULUS""\n")

x=int(input())
print("Enter first integer")
a=int(input())
print("Enter second integer")
b=int(input())

if x==1:
    summation(a,b)
elif x==2:
    substraction(a,b)
elif x==3:
    multiplication(a,b)
elif x==4:
    division(a,b)
else:
    modulus(a,b)