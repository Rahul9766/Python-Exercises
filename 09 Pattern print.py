# Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n=int(input("Enter range: "))

for i in range(1,n+1):
    print(f"{i} "*i)