# Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in
# a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
word='USA'
str1=str1.lower()
occurrence=str1.count(word.lower())
print(f"The {word} count is: {occurrence}")