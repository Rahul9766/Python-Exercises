# Print list in reverse order using a loop
# Given:

list1 = [10, 20, 30, 40, 50]
lst_len=len(list1)

for i in range(lst_len):
    print(list1[lst_len-i-1])
