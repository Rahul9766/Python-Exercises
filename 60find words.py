# Write a program to find words with both alphabets and numbers
# from an input string.

str1 = "Emma25 is Data scientist50 and AI Expert 57 "
lst=str1.split()
result=[]
for i in lst:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        result.append(i)

for i in result:
    print(i)

