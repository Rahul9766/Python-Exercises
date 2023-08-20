# mid row =n/2
# mid column == n//2



n=int(input("Enter number: "))

for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()