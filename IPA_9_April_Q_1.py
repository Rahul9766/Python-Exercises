'''
Remove the vowels from the given string and find the count of digits in the string
Example:
 Input:
 Hello World is the EmotiOn 3000

 Output:
 Modified string is Hll Wrld s th mtn 3000 and the Count of digits is 4

 
'''

a=input()
vowel="aeiouAEIOU"
digit="1234567890"
line=""
count=0
for i in a:
    if i in vowel:
        pass
    else:
        if i in digit:
           count+=1     
        line=line+i

print("Modified string is {line} and the Count of digits is {count}".format(line=line,count=count))
























# def fun1(s):
#     vowles="aeiouAEIOU"
#     digits = "0123456789"
#     result1=""
#     result2=[]

#     for i in s:
#         if i in vowles:
#             pass
#         else:
#             if i in digits:
#                 result2.append(1)
#             result1 = result1 + i
#     return result1 , sum(result2) 



# s=str(input())
# a,b=fun1(s)
# print("Modified string is {x} and the Count of digits is {y}".format(x=a,y=b))
