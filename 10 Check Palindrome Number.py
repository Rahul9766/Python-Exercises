# Write a program to check if the given number is a palindrome number.
#
# A palindrome number is a number that is same after reverse.
# For example 545, is the palindrome numbers

# def check_Palindrome(num):
#     print(f"Original Number: {num}")
#     ogNum=num
#     rev_num=0
#     while ogNum>0:
#         remainder=ogNum%10
#         rev_num=(rev_num*10)+remainder
#         ogNum=ogNum//10
#     print(f'reverse number: {rev_num}')
#     if num==rev_num:
#         print("number is palindrome")
#     else:
#         print("number is not palindrome")
#
# num=int(input("Enter number: "))
# check_Palindrome(num)

################################# Another way ######################################

def check_Palindrome(num):
    ogNum=str(num)
    rev_num=str(num)[::-1]
    if ogNum==rev_num:
        print("number is palindrome")
    else:
         print("number is not palindrome")



num=int(input("Enter number: "))
check_Palindrome(num)