# Write a program to display all prime numbers within a range
# Note: A Prime Number is a number that cannot be made by multiplying other whole numbers.
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
#
# Examples:
# 6 is not a prime mumber because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.

start=int(input("Enter number: "))
end=int(input("Enter number: "))
print("Prime Numbers: ")
flag=False
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j ==0:
                flag=True
                break
        else:
            print(i)

