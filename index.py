#Basic Calculator
import math

#This is a simple calculator that can perform basic operations such as addition, subtraction, multiplication, division, square and square root.
#The user will be asked to select an operation and enter the numbers on which the operation is to be performed.
def addition(num1, num2):
    return num1 + num2;

def subtraction(num1, num2):
    return num1 - num2;

def multiplication(num1, num2):
    return num1 * num2;

def division(num1, num2):
    return num1 / num2;

def square(num1):
    return num1 * num1;

def squareroot(num1):
    return math.sqrt(num1);

#Operations available for the user
print("Select operation:")
print("1.Addition\n")
print("2.Subtraction\n") 
print("3.Multiplication\n")
print("4.Division\n")
print("5.Square\n")
print("6.Square Root\n")

select = input("Select operations form 1, 2, 3, 4, 5, 6 :")

#User input
num1 = int(input("Enter first number: "));
num2 = int(input("Enter second number: "));

#Conditions for the operations
if select == '1':
    print(num1,"+",num2,"=",addition(num1,num2));
elif select == '2':
    print(num1,"-",num2,"=",subtraction(num1,num2));
elif select == '3':
    print(num1,"*",num2,"=",multiplication(num1,num2));
elif select == '4':
    if num2 != 0:
        print(num1,"/",num2,"=",division(num1,num2));
    else:
        print("Division by zero is not allowed");
elif select == '5':
    print(num1,"^2 =",square(num1));
elif select == '6':
        if num1 >= 0:
            print(num1,"=",squareroot(num1));
            