
# Iterate the given list of numbers and print only those numbers which are divisible by 5



def divisible(lst):
    for i in lst:
        if i%5==0:
            print(i)
        pass


lst=[23,545,65,4,5,35,46,56,34,60,105]
print("Divisible By 5")
divisible(lst)