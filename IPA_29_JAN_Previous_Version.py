'''
Question
Define a class to create a Team object with the below attributes:
teamRanking : of type integer representing the rank of the Team Eg: 10
teamConf : of the type String representing the Confederation of the Team Eg:"AFC"
teamName: of the type String representing the Name of the Team Eg:"Spain"
Define the method to initialize the attributes when a Team object is created.
Write the code to define a Class to Create a Tournament object with the below attributes:
1.A list containing elements of type Team.Eg-L=[T1,T2]
Where L is a list of Team objects T1 and T2.
2.Details of the Tournament , a dictionary containing the details of the Tournament in the format as
follows:
 {Name: "FIFA2022", Host:"Qatar",Edition: 22, Year: 2022,Participants:32,Time:1}
Define a method to initialize the attributes when a Tournament object is created.
Define the first method inside the Tournament class as below:
The method will find the count of Teams from each Confederation from the Team List present in the first
tournament of the Tournament list
and returns a dictionary having the confederation and teamCount (count of Teams) as key : value pairs.
Define the second method outside both the classes.
This method will take Number of times the Tournament was being hosted by the Host and a list of
Tournaments objects as parameters.

It will return the list of Teams from all the Tournaments from the list of Tournaments which has been
hosted(Time-given in the tournament details) same as the Number of times passed as a parameter.
If there is no Tournament in the given list which has the given host name as host in the Tournament,
the method should return None else it will return the List of Teams in ascending order of teamRanking
for each tournament object
i.e. If the Number of time is matching with the tournament A and tournament B present in the list of
Tournaments, the method will display the teamNames of all the Teams
from tournament A and tournament B in the ascending order of teamRanking.Please refer the sample
input and output below for more clarity.
Note : All String Comparison should be case insensitive.
Instructions to write main function:
You would require to write the main section completely, hence please follow the below instructions for
the same.
You would require to write the main program which is in line to the "sample input description section"
mentioned below and to read the data in the same sequence.
Create the respective objects of the classes defined referring to the below instructions.
Main Function Instructions:
A. Create a list of Tournament objects which will be passed as argument while calling the function in
main. To create the list:
1.Read a number for the count of Tournament objects to be created and added to the list.
2.Create a Tournament object to be added to the list. To create the Tournament object, do the
following:
2.1 Read a number for the count of Team objects to be added to the list of Team objects for the
Tournament objects.
2.2 Create a Team object after reading the data (teamRanking, teamConf, the name of the team) related
to it and add to the list of Team objects.
This point repeats for the count of Team objects to be created as per point #A.2.1.
2.3 Read values for attributes such as Name,Host,Edition,Year,Participants and Time which are for the
dictionary that you are passing as an parameter
when you create the Tournament objects.Considering these attributes as keys, store the values read as
key : value pairs in a dictionary for the details.

Eg.{Name: "FIFA2022", Host:"Qatar",Edition: 22, Year: 2022,Participants:32,Time:1}
2.4 Create a tournament object by passing the list of Team objects and dictionary created above and add
it to the Tournament list.
3. This repeats for the number of Tournament objects to be created (considered in the first line of
input) as per point #A.1.
B. Read an integer value as input depicting Number of times to be passed as argument to the second
function(function defined outside the class).
C. Call the first method to find count of Teams confederation wise mentioned above from the main
section using the first element of the List of Tournament objects created in point #A(i.e the First
tournament Object created)
D. Display the values returned by the above function. Display the Confedeartion names and count of
Team returned by the function as per the requirement given.
E. Call the second function from the main section, by passing the times and the list of tournament
objects created above.
F. Display the list of team names returned by the second function.
- If function returns None, then display “No Team Found” (excluding the quotes).
Sample Input (below) description:
1.The first input taken in the main section is the number of Tournament Objects to be created(suppose
n).
2.The next set of inputs are related to n Tournament objects to be created as follows:
2.1 Count of Team objects(Suppose m) to be created and added to the list of Teams for the Tournament.
2.2 The next set of inputs are values for attributes of m teams -teamRanking, teamConf, teamName (for
each team object taken one after other and is repeated for m number of team objects).
2.3 Next set of values are for the following keys of the address for the Tournament object .
Name
Host
Edition
Year
Participants
Time
3. Last line of input represents the integer -Time, supplied as a argument to the second function.

You can use/refer the below given sample input and output for more details of the format for input and
output.
Consider below sample input and output to test your code:


**********************************************************************************
Input-1:
3
3
23
OFC
Australia
168
AFC
Bangladesh
90
AFC
Mongolia
AsiaSeries2020
India
7
2020
3
1
4
5
SA
Argentina
2
UEFA
England
6
UEFA
Portugal
16
UEFA
Netherlands
EuroCup2021
England
7
2021
4
1
3
56
UEFA
Wales
13
UEFA
Sweden
89
CAF
Nigeria
KnockoutCup2022
India
7
2022
3
1
1

Output-1:
OFC - 1
AFC - 2
England
Argentina
Portugal
Sweden
Netherlands
Australia
Wales
Nigeria
Mongolia
Bangladesh



Input-2:
2
3
12
UEFA
Portugal
106
AFC
India
86
AFC
China
TriNationSeries2020
India
7
2020
3
3
4
1
SA
Argentina
5
UEFA
England
12
UEFA
Portugal
3
UEFA
Netherlands
ChampionsCup2021
England
7
2021
4
2
3


Output-2:
UEFA - 1
AFC - 2
Portugal
China
India

Input-3:
3
3
22
UEFA
France
189
NA
Canada
99
AFC
Mongolia
AsiaSeries2020
India
7
2020
3
2
4
5
SA
Argentina
2
UEFA
England
4
UEFA
Portugal
19
UEFA
Netherlands
EuroCup2021
England
7
2021
4
2
3
56
UEFA
Wales
13
UEFA
Sweden
89
CAF
Nigeria
KnockoutCup2022
India
7
2022
3
1
2


Output-3:
UEFA - 1
NA - 1
AFC - 1
England
Portugal
Argentina
Netherlands
France
Mongolia
Canada

Input-4:
2
3
12
UEFA
Portugal
106
AFC
India
86
AFC
China
TriNationSeries2020
India
7
2020
3
3
4
1
SA
Argentina
5
UEFA
England
12
UEFA
Portugal
3
UEFA
Netherlands
ChampionsCup2021
England
7
2021
4
2
3

Output-4:
UEFA - 1
AFC - 2
Portugal
China
India


'''

        
def CountTeamsForEachConfederation(TourList):
    arr = TourList[0][0]
    X=[]
    Res={}
    for i in range(len(arr)):
        X.append(arr[i][1])

    R=set(X)
    R=sorted(R,reverse=True)
    for i in R:
        q=X.count((i))
        print('{i} - {ans}'.format(i=i,ans=X.count(i)))


def PrintTeam(TourList,time):
    result=[]
    flag=False
    for i in range(len(TourList)):
        arr1 = TourList[i]
        arr2=arr1[0]
        arr3=arr1[1]
        if arr3['Time']==time:
            flag=True
            for i in range(len(arr2)):
                result.append(arr2[i])

    if flag:
        result.sort()
        for i in range(len(result)):
            print(result[i][2])
    else:
        print("No Team Found")


#first line of input contains number of tournaments
No_Tournaments=int(input())

#TourList contains List of tournament
TourList=[]

#take input for each tournament
while No_Tournaments!=0:

    #tour_att is the list that contains two paraameters 
    # 1)List of m teams with attributes >TeamRanking  >TeamConfederation  >TeamName
    # 2)Dictionary that contains information of tournament with attribute  >Name(string) >HOst(string) >Edition(int) >Year(int) >Participants(int) >Time(int)
    Tour_att=[]

    #take input for number of teams
    no_team = int(input())

    team=[]
    for i in range(no_team):
        team_att = []

        team_att.append(int(input()))   #teamRanking
        team_att.append(str(input()))   #teamConf
        team_att.append(str(input()))   #teamName
        team.append(team_att)
    Tour_att.append(team)
    
    tour_Dict={}
    tour_Dict["Name"] = input()
    tour_Dict["Host"] = input()
    tour_Dict["Edition"] = int(input())
    tour_Dict["Year"] = int(input())
    tour_Dict["Participants"] = int(input())
    tour_Dict["Time"] = int(input())
    Tour_att.append(tour_Dict)

    TourList.append(Tour_att)
    No_Tournaments-=1

# print(TourList)
time=int(input())
CountTeamsForEachConfederation(TourList)
PrintTeam(TourList,time)
