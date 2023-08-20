# String characters balance Test
# Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all
# the characters in the s1 are
# present in s2. The character’s position doesn’t matter.

def balance_check(s1,s2):
    len_s1=len(s1)
    count=0
    for i in s1:
        if i in s2:
            count+=1
    if count==len_s1:
        return True
    else:
        return False



s1 = "Yn"
s2 = "PYnative"
flag = balance_check(s1,s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = balance_check(s1,s2)
print("s1 and s2 are balanced:", flag)