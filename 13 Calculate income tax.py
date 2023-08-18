# Calculate income tax for the given income by adhering to the below rules
# Taxable    Income	    Rate (in %)
# First     $10,000	        0
# Next      $10,000	        10
# Then      remaining	    20

# Expected Output:
# For example, suppose the taxable income is 45000 the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.



def incometax(income):
    tax=0
    if income<=10000:
        print("Total tax to pay is",tax)
    elif income>10000 and income<=20000:
        remaining=income-10000
        tax=(10000*0)+(remaining*10/100)
        print("Total tax to pay is",tax)
    elif income>20000:
        remaining = income - 20000
        tax = (10000 * 0)+(10000 * 10 / 100)+(remaining*20/100)
        print("Total tax to pay is",tax)



income=int(input("Enter Income: "))
incometax(income)
