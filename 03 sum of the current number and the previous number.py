# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.

n=int(input("Enter range: "))

for i in range(10):
    if i==0:
        print(f"Current number: {i} Previous Number: {i} Sum is: {i}")
    else:
        print(f"Current number: {i} Previous Number: {i-1} Sum is: {i+i-1}")