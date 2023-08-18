
# Write a program to accept a string from the user and display
# characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

sentence=input("Enter String:")

for count,character in enumerate(sentence):
    if count%2==0:
        print(character)
    pass