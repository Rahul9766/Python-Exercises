# Write a program to print the following start pattern using the for loop
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


num=int(input("Enter number: "))

for i in range(num):
    for j in range(i):
        print("*",end='')
    print()
for i in range(num):
    for j in range(num-i):
        print("*",end='')
    print()