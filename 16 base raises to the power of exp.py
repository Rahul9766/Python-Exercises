# Write a function called exponent(base, exp) that returns
# an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.



def exponent(base,exp):
    if exp <0:
        print("exp is a negative integer enter valid number")
    else:
        print(f"{base} raises to the power of {exp}: {base**exp}")




base=int(input("Enter Base: "))
exp=int(input("Enter Exponent: "))
exponent(base,exp)