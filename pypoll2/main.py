import os
import csv

"""
The dataset is composed of three columns: 
Voter ID, County, and Candidate. 

Your task is to create a Python script that 
1. analyzes the votes and 
2. calculates each of the following:
    2a. The total number of votes cast
    2b. A complete list of candidates who received votes
    2c. The percentage of votes each candidate won
    2d. The total number of votes each candidate won
    2e. The winner of the election based on popular vote.

#Results should look similar to:

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

csvpath = os.path.join("election_data.csv")

Election_Results = str("Election Results")
print(Election_Results)
#Create a variable to hold the divider
Break_Lines = str("--------------------------")
print(Break_Lines)

"""
Approach_Total_Votes:
1. Create a dictionary of the 3 column csv where col1 Voter ID corresponds as the key to the col3 Candidate. 
1a. And col2 is omitted, as we do not need this data
2. Calculate the total number of votes cast by counting the number of keys in the created dictionary 
"""
with open(csvpath, newline="") as csvfile:
    next(csvfile) #skip header
    csvreader = csv.reader(csvfile,delimiter=",")
    #writer = csv.writer(csvfile)
    #mydict = {rows[0]: rows[1] for rows in csvreader}
    #print(mydict)
    #for v,c,d  in reader:
#Approach_Total_Votes: 1
    dict_result = {}
    for row in csvreader:
        key = row[0]
        #if key in result:
            # implement your duplicate row handling here
           # pass
        dict_result[key] = row[2:]
#Approach_Total_Votes: 2
    #How to account for accidental duplicate voting? would the above hashtagged "if key in result" do this?
#Set ensures there are no repeats
Total_Votes = len(set(dict_result))
Total_Votes_Text = str(f"Total Votes: {Total_Votes}")
print(Total_Votes_Text)
print(Break_Lines)
#print(dict_result)

with open(csvpath, newline="") as csvfile:
    next(csvfile) #skip header
    csvreader = csv.reader(csvfile,delimiter=",")
    #election_list = list(csvreader)
    #print(election_list)
"""
Approach Complete_Candid
Calculate the complete list of candidates who received votes
1. Iterate through the third value (csv col3) of dictionary and collect all unique names (skip duplicates) 
2. Store in a list
"""

#Approach Complete_Candid
#1. Iterate through dict_result dictionary, extract values (omit keys) and return only unique values.
# Store in list variable.
with open(csvpath, newline="") as csvfile:
    next(csvfile) #skip header
    csvreader = csv.reader(csvfile,delimiter=",")
#Create list of candidates with no repetitions so we can see the shortlist of candidates who ran
    Candidates_List_Unique = (list(set([x[0] for x in dict_result.values()])))
    #print(Candidates_List_Unique)
#Create list of only candidates (with reptitions) so we can use this to tally/count the votes per candidate
    Candidates_List = (list(x[0] for x in dict_result.values()))
    #print(Candidates_List)
#Count number of appearances (votes) for each candidate
#Count the votes per candidate
#Import Counter function
    from collections import Counter
#Variable = Count each candidate in the Candidates_List
    c = Counter(Candidates_List)
#Print each candidate with corresponding vote count
    #print(c)
        #d = list(c) - this created a list of only the 4 names, similar to the Candidates_List_Unique
         #print(d)
#Variable = each candidate with corresponding percentage vote in descending order
    cand_order_percentage = list([(i, c[i], (c[i] / len(Candidates_List) * 100.0)) for i, count in c.most_common()])
          #original:     cand_order_percentage = list([(i, c[i] / len(Candidates_List) * 100.0) for i, count in c.most_common()])
          #print(cand_order_percentage)
    #for x,y,z in cand_order_percentage:
              #print(f"{x}: {format(z,'.3f')}% ({y})")
        #Election_Votes_Text = (f"{x}: {format(z,'.3f')}% ({y})")
        #print(Election_Votes_Text)
    Election_Votes_Text_2 = [(f"{x}: {format(z,'.3f')}% ({y})") for x,y,z in cand_order_percentage]
    #print(Election_Votes_Text_2)
    #print(Election_Votes_Text_2[0])
    Election_Votes_Text_Khan1 = str(Election_Votes_Text_2[0])
    print(Election_Votes_Text_Khan1)
    #print(Election_Votes_Text_2[1])
    Election_Votes_Text_Correy2 = str(Election_Votes_Text_2[1])
    print(Election_Votes_Text_Correy2)
    #print(Election_Votes_Text_2[2])
    Election_Votes_Text_Li3 = str(Election_Votes_Text_2[2])
    print(Election_Votes_Text_Li3)
    #print(Election_Votes_Text_2[3])
    Election_Votes_Text_OTooley4 = str(Election_Votes_Text_2[3])
    print(Election_Votes_Text_OTooley4)
    #print(c["Khan"]) - works bc  c= dictionary
    #print(cand_order_percentage["Khan"]) doesn't work because c_o_p = list

#To find most/highest occurrence of items in the python list // For highest item
    print(Break_Lines)
    k = c.most_common()
    winner_candidate = (k[0][0])
    Winner_Candidate_Text = str((f"Winner: {winner_candidate}"))
    print(Winner_Candidate_Text)
    print(Break_Lines)

print()
#Instruction: your final script should both print the analysis to the terminal and export a text file with the results.
#I ask the user if they'd like to create and export a text file of the results, just to be nice and polite and stuff.
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