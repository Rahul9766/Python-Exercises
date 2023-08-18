# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or
# lower than 1000, else return their sum.

number1=int(input("num1: "))
number2=int(input("num2: "))

sum=number1+number2
sub=number1-number2
mul=number1*number2
div=number1/number2

print(f"Sum is {sum}")
print(f"Subtraction is {sub}")
print(f"Multiplication is {mul}")
print(f"Division is {div}")