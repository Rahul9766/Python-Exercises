
'''
2 Complex Python Program
2.1 Problem Statement
Define a class to create objects of type MovieInfo that has the following attributes:
Title-Title should be of the type String; representing title of the movie.Eg: Coda
Year-Year should be of the type Integer;representing the year movie was released. Eg:2021
Awards-Awards should be of the type Integer;representing the number of awards the movie
has won.Eg:3
Nomination-Nominations should be of the type Integer;representing the number of
nominations the movie was nominated for.Eg:3
Country-Country should be of the type String; representing the movie origin country .Eg:Italy
Define the __init__ method to initialize the attributes of the objects to be created.
Create another class Award with following attributes:
a. List of MovieInfo Objects. Eg: For example if lst is a list containing 2 objects i.e.lst=[m1,m2]
where m1 and m2 are 2 different MovieInfo Objects.
Create below functions inside the Award class:
1. The first method takes in year (Type-Integer) and returns details of all non-American
movies that have won awards in that year specified.
 Note: All string comparisons should be case insensitive.
2. The second method uses the information from MovieInfo class and creates a dictionary
that keeps movies titles as keys and success rate as values. It then sorts the dictionary in
descending order based on values. This method returns a sorted dictionary.
For example: Success Rate calculation for the above data:
Number of nominations=3
Number of awards=3
Success rate=(Number of awards/Number of nominations)*100=(3/3)*100=100
 Note: Success rate must be an integer value
Instructions to write main section of the code:
a. You would require to write the main section completely, hence please follow the below
instructions for the same.
b. You would require to write the main program which is inline to the ""sample input
description section"" mentioned below and to read the data in the same sequence.
c. Create the respective objects (MovieInfo, Award)with the given sequence of arguments to
fulfill the __init__ method requirement defined in the respective classes referring to the below
instructions.
 1. First create a list of MovieInfo objects,to do so:
 i. Read a number for the count of MovieInfo objects to be created.
 ii. Create a MovieInfo object after reading the data related to it and add the object to
the list of MovieInfo objects. This point repeats for the number of MovieInfo objects
(considered in the first line of input)
2. Create an object of the class Award using the list of MovieInfo.
d. Read the year (Type-Integer).
e. Call the methods described above from the main section with appropriate values as
arguments from the main section.
f. Display MovieInfo details that matches the input read. You may refer to the sample output
for the display format. If method returns None, then display the message ‘No Movie found'
(excluding the quotes).
g. Display the sorted dictionary (sorted in descending order based on Values) consisting of
movie titles as key and the success rate as values. You may refer to the sample output for the
display format. If method returns None, then display the message ‘Unable to create dictionary'
(excluding the quotes).
Input Format for Custom Testing
 a. The 1st input taken in the main section is the number of MovieInfo objects to be added
to the list of MovieInfo, say x.
 b. The next line of input is the title of the movie.
 c. Next input denotes the year the movie was released.
 d. The next input denotes the number of Awards won by the movie.
 e. Next line of input is the number of nominations the movie received.
 f. Next line of input is the country of origin the movie was made.
 Point b to f is repeated for x times (where x is the number of MovieInfo objects given in the
first line of input).
 g. The next line of input refers to the year which is to be passed as argument to the first
method.
You can consider below sample input and output to verify your implementation before
submission.


*****************************************************************************************************

*******testcase-1:***********
8
Coda
2021
3
3
Italy
Drive my car
2021
1
4
Japan
Tenet
2020
1
2
America
Soul
2020
2
3
America
Mank
2020
2
10
America
Marriage Story
2019
1
6
America
Birdman
2014
4
9
America
Belfast
2021
1
7
Britain
2021


*****************OP-1************

Coda
2021
3
3
Italy
Drive my car
2021
1
4
Japan
Belfast
2021
1
7
Britain
Coda 100
Soul 66
Tenet 50
Birdman 44
Drive my car 25
Mank 20
Marriage Story 16
Belfast 14

***************Testcase-2******************

8
Coda
2021
3
3
Italy
Drive my car
2021
1
4
Japan
Tenet
2020
1
2
America
Soul
2020
2
3
America
Mank
2020
2
10
America
Marriage Story
2019
1
6
America
Birdman
2014
4
9
America
Belfast
2021
1
7
Britain
2020



***********OP-2**********
No Movie found
Coda 100
Soul 66
Tenet 50
Birdman 44
Drive my car 25
Mank 20
Marriage Story 16
Belfast 14


*********Testcase-3********

8
Coda
2021
3
3
Italy
Drive my car
2021
1
4
Japan
Tenet
2020
1
2
America
Soul
2020
2
3
America
Mank
2020
2
10
America
Marriage Story
2019
1
6
America
Birdman
2014
4
9
America
Belfast
2021
1
7
Britain
2000


********OP-3***********

No Movie found
Coda 100
Soul 66
Tenet 50
Birdman 44
Drive my car 25
Mank 20
Marriage Story 16
Belfast 14


**********Testcase-4*********

0
2021

*****OP-4******

No Movie found
Unable to create dictionary


'''


# def function1(y,Award):
#     flag=False
#     for i in Award:
#         if (i[1] == y) and (i[4] != 'America'):
#             flag=True
#             for j in range(len(i)):
#                 print(i[j])

#     if not flag:
#         print("No Movie found")


# def function2(Award):
#     Res={}
#     for i in Award:
#         nomination = i[3]
#         awards = i[2]
#         success_rate = int((awards/nomination)*100)
#         Res[i[0]] = int(success_rate)

#     if not len(Res):
#         print("Unable to create dictionary")
#     else:
#         for p,q in sorted(Res.items(),key = lambda x:x[1],reverse=True):
#             print(p,q)



# n=int(input())
# Award=[]
# for i in range(n):
#     MovieInfo=[]
#     MovieInfo.append(input())   #title
#     MovieInfo.append(int(input()))  #year
#     MovieInfo.append(int(input()))  #award
#     MovieInfo.append(int(input()))  #Nomination
#     MovieInfo.append(input())   #Country
#     Award.append(MovieInfo)


# in_year = int(input())
# function1(in_year,Award)
# function2(Award)


def nonAmericanMovie(year, award):
    result=[]
    for i in range (len(award)):
        arr=award[i]
        if arr[1] == year and arr[4] != "America":
            result.append(arr)
            
    for i in range (len(result)):
        print(result[i][0])
        print(result[i][1])
        print(result[i][2])
        print(result[i][3])
        print(result[i][4])

def successmovie(Success):
    sorted_list=sorted(Success, key=lambda x: x[1], reverse=True)
    for i in range (len(sorted_list)):
        p=sorted_list[i][0]
        q=sorted_list[i][1]
        print(p,q)


noOfMovies=int(input())

award=[]
Success=[]


for i in range (noOfMovies):
    MovieInfo=[]
    Title=input()
    Year=int(input())
    Awards=int(input())
    Nomination=int(input())
    Country=input()
    MovieInfo.append(Title)
    MovieInfo.append(Year)
    MovieInfo.append(Awards)
    MovieInfo.append(Nomination)
    MovieInfo.append(Country)
    award.append(MovieInfo)
    
    SuccessRate =int((Awards/Nomination)*100)    
    dict=[]
    dict.append(Title)
    dict.append(SuccessRate)
    Success.append(dict)
    
    
    
year=int(input())
nonAmericanMovie(year, award)
successmovie(Success)