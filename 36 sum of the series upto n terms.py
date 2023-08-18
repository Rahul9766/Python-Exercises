# Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term.
# For example,
# if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

num=int(input("Enter number: "))
start=2
sum=0
for i in range(1,num+1):
    print(start,end='+')
    sum+=start
    start=start*10+2


print("\nSum of above series is:", sum)






