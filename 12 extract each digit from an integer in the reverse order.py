# Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with
# a space separating the digits.

# def rev_num(n):
#     number=n
#     rev_number = 0
#     while number>0:
#         remainder=number%10
#         rev_number=(rev_number*10)+remainder
#         number=number//10
#     rev_str=str(rev_number)
#     for i in rev_str:
#         print(i,end=" ")
#
# n=int(input())
# rev_num(n)


#############################Another Way####################


def rev_num(n):
    num=str(n)[::-1]
    for i in num:
        print(i,end=" ")

n=int(input())

rev_num(n)