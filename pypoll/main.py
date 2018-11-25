
import os
import csv

csvpath = os.path.join("election_data.csv")

Election_Results = str("Election Results")
print(Election_Results)
Break_Lines = str("--------------------------")
print(Break_Lines)

with open(csvpath, newline="") as csvfile:
    next(csvfile) #skip header
    csvreader = csv.reader(csvfile,delimiter=",")
    dict_result = {}
    for row in csvreader:
        key = row[0]
        dict_result[key] = row[2:]

Total_Votes = len(set(dict_result))
Total_Votes_Text = str(f"Total Votes: {Total_Votes}")
print(Total_Votes_Text)
print(Break_Lines)

with open(csvpath, newline="") as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile,delimiter=",")

    Candidates_List_Unique = (list(set([x[0] for x in dict_result.values()])))
    Candidates_List = (list(x[0] for x in dict_result.values()))
    from collections import Counter
    c = Counter(Candidates_List)
    cand_order_percentage = list([(i, c[i], (c[i] / len(Candidates_List) * 100.0)) for i, count in c.most_common()])
    Election_Votes_Text_2 = [(f"{x}: {format(z,'.3f')}% ({y})") for x,y,z in cand_order_percentage]
    Election_Votes_Text_Khan1 = str(Election_Votes_Text_2[0])
    print(Election_Votes_Text_Khan1)
    Election_Votes_Text_Correy2 = str(Election_Votes_Text_2[1])
    print(Election_Votes_Text_Correy2)
    Election_Votes_Text_Li3 = str(Election_Votes_Text_2[2])
    print(Election_Votes_Text_Li3)
    Election_Votes_Text_OTooley4 = str(Election_Votes_Text_2[3])
    print(Election_Votes_Text_OTooley4)
    print(Break_Lines)

    k = c.most_common()
    winner_candidate = (k[0][0])
    Winner_Candidate_Text = str((f"Winner: {winner_candidate}"))
    print(Winner_Candidate_Text)
    print(Break_Lines)

print()

Output_Text = input("Would you like to export a text file of the results? If yes, type 'y':")
if Output_Text == 'y':
    print("Okay, a text file of the results has been exported as 'pythonhw1_pypoll_results_2018.txt'")
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
    print("Okay, a text file of the results will *not* be exported :)")