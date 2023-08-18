import random

def win(comp,you):
    if comp == you:
        return None
    elif comp=="Rock":
        if you=="Scissors":
            return False
        elif you=="Paper" :
            return True
        else:
            print("Give Correct Input")
            
        
    elif comp=="Paper":
        if you=="Rock":
            return False
        elif you=="Scissors":
            return True
        else:
            print("Give Correct Input")
        
    elif comp=="Scissors":
        if you=="Paper":
            return False
        elif you=="Rock":
            return True
        else:
            print("Give Correct Input")


print("Comp Turns Will chose Rock Paper Scissors\n")

comp =random.randint(1,3)
if (comp ==1):
    comp="Rock"
elif (comp ==2):
    comp="Paper"
elif (comp ==3):
    comp="Scissors"

you= input("It's Your Turn Choose  Rock Paper or Scissors: ")

decision = win(comp,you)

if decision == None:
    print(f"Match is Tie Bcoz Comp Chose: {comp} and You Chose: {you}")   
elif decision==True :
    print(f"You Win!!!! Bcoz Comp Chose: {comp} and You Chose: {you}")   
elif decision==False :
    print(f"Comp is Winner!!! Bcoz Comp Chose: {comp} and You Chose: {you}")
    



