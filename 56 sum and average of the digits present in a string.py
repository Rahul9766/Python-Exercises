# Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average
# of the digits that appear in the string, ignoring all other characters.

str1 = "PYnative29@#8496"
total=0
count=0
for i in str1:
    if i.isdigit():
        total=total+int(i)
        count+=1

avg = total / count
print("Sum is:", total, "Average is ", avg)