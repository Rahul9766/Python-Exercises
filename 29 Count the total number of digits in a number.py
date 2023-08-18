# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.

n=int(input("Enter number: "))
count=0
while n>0:
    n=n//10
    count+=1

print(count)
