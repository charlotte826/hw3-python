"""
PyPoll HW Checklist:
1. Import CSV File (budget_data.csv)
1a. Open and Read CSV File (The dataset is composed of three columns: Voter ID, County, and Candidate.)
2. Print Election Results
3. Print (----------------------------)
4. Calculate the total number of votes cast
4a. Print (Total Votes: 3521001)
5. Print (----------------------------)
6. Create a complete list of candidates who received votes
7. Calculate the percentage of votes each candidate won
8. Calculate the total number of votes each candidate won
9. Print #6-8 election results per candidate
9a. Print (Khan: 63.000% (2218231))
9b. Print (Correy: 20.000% (704200))
9c. Print (Li: 14.000% (492940))
9d. Print (O'Tooley: 3.000% (105630))
10. Print (-------------------------)
11. Calculate the winner of the election based on popular vote.
11a. Print (Winner: Khan)
12. Print (-------------------------)
13**. Your final script should both print the analysis to the terminal
14**. Export a text file with the results

** Results should look similar to:

Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
"""
#1. Import & Read CSV File ("election_data.csv")
import os
import csv

csvpath = os.path.join("election_data.csv")

Election_Results = str("Election Results")
#2. Print Election Results
print(Election_Results)
Break_Lines = str("--------------------------")
#3. Print (----------------------------)
print(Break_Lines)

"""
    Approach_Total_Votes:
    1. Create a dictionary of the csv where col1 'Voter ID' corresponds as key to the col3 'Candidate'. 
    1a. Col2 'County' is omitted, as we do not need this data
    2. Calculate the total number of votes cast 
    2b. Count the number of keys in the created dictionary (key='Voter ID'Value=IndividualVote)
"""
#1a. Open and Read CSV File
with open(csvpath, newline="") as csvfile:
    next(csvfile) #skip header
    csvreader = csv.reader(csvfile,delimiter=",")
    dict_result = {}
    for row in csvreader:
        key = row[0]
        #if key in result:
            # implement your duplicate row handling here
           # pass
        dict_result[key] = row[2:]
    #Approach_Total_Votes: 2
    #How to account for accidental duplicate voting? Would above hashtagged "if key in result" do this?
#4. Calculate the total number of votes cast
Total_Votes = len(set(dict_result)) #Set ensures there are no repeats; len counts the votes
Total_Votes_Text = str(f"Total Votes: {Total_Votes}")
#4a. Print (Total Votes: 3521001)
print(Total_Votes_Text)
#5. Print (----------------------------)
print(Break_Lines)


#6. Create a complete list of candidates who received votes
#7. Calculate the percentage of votes each candidate won
#8. Calculate the total number of votes each candidate won

"""
    Approach_Complete_Candidate 
    1. Calculate the complete list of candidates who received votes
     1a. Store only unique instances of 'Candidate' in a list variable (Candidates_List_Unique)
     1b. Iterate through the 'Candidate' values of created dictionary (dict_result)
     1c. Skip duplicates
     1d. Collect only unique instances of 'Candidate' names 
    2. Calculate the total number of votes each candidate won
     2a. Create a list (Candidates_List) containing all 'Candidate' values from created dictionary (dict_result)
     2b. 
"""

with open(csvpath, newline="") as csvfile:
    next(csvfile) #skip header
    csvreader = csv.reader(csvfile,delimiter=",")
    #Approach_Complete_Candidate: 1
#6. Create a complete list of candidates who received votes
    Candidates_List_Unique = (list(set([x[0] for x in dict_result.values()]))) #List of unique instances of 'Candidate' in a list variable
    #Approach_Complete_Candidate: 2
    Candidates_List = (list(x[0] for x in dict_result.values())) #List of 'Candidate' values (with reptitions)
#8. Calculate the total number of votes each candidate won
    from collections import Counter
    c = Counter(Candidates_List) #c = Tally each instance of 'Candidate' in 'Candidate'_List
    #cand_order_percentage = List each candidate with corresponding percentage vote and vote count in descending order
#7. Calculate the percentage of votes each candidate won
    cand_order_percentage = list([(i, c[i], (c[i] / len(Candidates_List) * 100.0)) for i, count in c.most_common()])
    #Election_Votes_Text_2 = format candidate, percentage and vote count
#9. Print #6-8 election results per candidate
    Election_Votes_Text_2 = [(f"{x}: {format(z,'.3f')}% ({y})") for x,y,z in cand_order_percentage]
    Election_Votes_Text_Khan1 = str(Election_Votes_Text_2[0])
#9a.Print(Khan: 63.000 % (2218231))
    print(Election_Votes_Text_Khan1)
    Election_Votes_Text_Correy2 = str(Election_Votes_Text_2[1])
#9b.Print(Correy: 20.000 % (704200))
    print(Election_Votes_Text_Correy2)
    Election_Votes_Text_Li3 = str(Election_Votes_Text_2[2])
#9c.Print(Li: 14.000 % (492940))
    print(Election_Votes_Text_Li3)
    Election_Votes_Text_OTooley4 = str(Election_Votes_Text_2[3])
#9d. Print (O'Tooley: 3.000% (105630))
    print(Election_Votes_Text_OTooley4)
#10. Print (-------------------------)
    print(Break_Lines)

#11. Calculate the winner of the election based on popular vote.
    k = c.most_common() #Define identifier of most frequent occurrence of *item or number* in Candidates_List
                        # (connects to c/Counter above)
    winner_candidate = (k[0][0]) #Identifies *item* of highest frequency in Candidates_List
    Winner_Candidate_Text = str((f"Winner: {winner_candidate}"))
#11a. Print (Winner: Khan)
    print(Winner_Candidate_Text)
#12. Print (-------------------------)
    print(Break_Lines)

print()
#13**. Your final script should both print the analysis to the terminal
#14**. Export a text file with the results
    #I ask the user if they'd like to create and export a text file of the results.
Output_Text = input("Would you like to export a text file of the results? If yes, type 'y':")
if Output_Text == 'y':
    f = open('pythonhw1_pypoll_results_2018.txt','w')
    f.write(Election_Results
            + "\n" +
            Break_Lines
            + "\n" +
            Total_Votes_Text
            + "\n" +
            Break_Lines
            + "\n" +
            Election_Votes_Text_Khan1
            + "\n" +
            Election_Votes_Text_Correy2
            + "\n" +
            Election_Votes_Text_Li3
            + "\n" +
            Election_Votes_Text_OTooley4
            + "\n" +
            Break_Lines
            + "\n" +
            Winner_Candidate_Text
            + "\n" +
            Break_Lines
            )
    f.close()
else:
    print("Okay, a text file of the results will not be exported :)")