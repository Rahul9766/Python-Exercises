# Write a program to find how many times substring “Emma” appears in the given string.
#
# Given:
# "Emma is good developer. Emma is a writer"
#

str_x = "Emma is good developer. Emma is a writer"
sub_str=input()
str_lst=str_x.split()
count=0
for i in str_lst:
    if i==sub_str:
        count+=1

print(f'count: {count}')

