# Write a program to use the loop to find the factorial of a given number.
#
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
#
# For example: calculate the factorial of 5
#
# 5! = 5 × 4 × 3 × 2 × 1 = 120

num=int(input("Enter number: "))
og_num=num
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num):
        num=num*i
    print("The factorial of", og_num, "is", num)