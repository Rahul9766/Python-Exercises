# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.
#
# Given:
#
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
#
#

def checkList(lst):
    first=lst[0]
    last=lst[-1]
    if first == last :
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("Result is "+str(checkList(numbers_x)))
numbers_y = [75, 65, 35, 75, 30]
print("Result is "+str(checkList(numbers_y)))
