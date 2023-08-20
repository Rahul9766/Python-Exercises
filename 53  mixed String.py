# Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a
# new string s3 made of the first char of s1, then the last char of s2,
# Next, the second char of s1 and second last char of s2,
# and so on. Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"

s2=s2[::-1]
l= len(s1) if len(s1) > len(s2) else len(s2)
result=""
for i in range(l):
    if i<len(s1):
        result=result+s1[i]
    if i<len(s2):
        result=result+s2[i]
print(result)