# Print the following pattern
# Write a program to print the following number pattern using a loop.
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=int(input("Enter number: "))

for i in range(n):
    for j in range(i+1):
        print(i+1,end=' ')
    print()