"""
PyBank HW Checklist:
1. Import CSV File (budget_data.csv)
1a. Open and Read CSV File
2. Print (Financial Analysis)
3. Print (----------------------------)
4. Calculate: The total number of months included in the dataset
4a. Print (Total Months: 86)
5. Calculate: The total net amount of "Profit/Losses" over the entire period
5a. Print (Total: $38382578)
6. Calculate: The average change in "Profit/Losses" between months over the entire period
6a. Print (Average Change: $-2315.12)
7. Calculate: The greatest increase in profits (date and amount) over the entire period
7a. Print (Greatest Increase in Profits: Feb-2012 ($1926159))
8. Calculate: The greatest decrease in losses (date and amount) over the entire period
8a. Print (Greatest Decrease in Profits: Sep-2013 ($-2196167))
9**. Your final script should both print the analysis to the terminal
10**. Export a text file with the results

** As an example, your analysis should look similar to the one below:

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""

#1. Import & Read CSV File (budget_data.csv)
import os
import csv

csvpath = os.path.join("budget_data.csv") #csv file in quotes because csv file is copied to same folder that contains main.py (current file)

#2. Print (Financial Analysis)
Financial_Analysis = ("Financial Analysis")
print(Financial_Analysis)
#3. Print (----------------------------)
Break_Lines = ("--------------------------")
print(Break_Lines)

#1a. Open and Read CSV File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

#4. Calculate: The total number of months included in the dataset
    #Count lines of csv. Each csv line (minus header) = one month
    next(csvfile) #skip count of the header row of csv file (approach #1)
    row_count = sum(1 for line in csvreader)
    Total_Months = ("Total Months: " + str(row_count))
#4a. Print (Total Months: 86)
    print(Total_Months)

    #Difficulty returning results; open/read csv file again. Indentation/block issue?
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#5. Calculate: The total net amount of "Profit/Losses" over the entire period
    #Create variable list to hold all 'Profit/Losses' values
    net_profit_list = []
    #Populate the list(net_profit_list): Loop through csv to grab only the 'Profit/Losses' column values of csv. Add to list(net_profit_list)
    for rows in csvreader:
         net_profit_list.append(rows[1])
    net_profit_list.remove('Profit/Losses') #Remove the header (approach #2)
    #Convert list elements into integers so we can sum(net_profit_list)
    net_profit_list = [int(rows) for rows in net_profit_list]
    #print(net_profit_list[0:9])
    #Create variable to house sum(net_profit_list)
    total_net_value = str(sum(net_profit_list))
    Total_Net = (f"Total: ${total_net_value}")
#5a. Print (Total: $38382578)
    print(Total_Net)

        # Second approach that successfully calculates sum(net_profit_list)

        #def listsum(net_profit_list):
           # theSum = 0
            #for x in net_profit_list:
             #   theSum = theSum + x
           # return theSum
        #print(listsum(net_profit_list))

#6. Calculate: The average change in "Profit/Losses" between months over the entire period
    """
    Approach
    1. Create a formula to find the change in Profit/Losses between each month over the entire period
    2. To find the change between each month, I will want to:
     2a. subtract the first element (first month profit/loss) in the list from the second element (second month profit/loss)
     2b. subtract the second element from the third element
     2c. and so forth, continuing this pattern, iterating over the entire list of net_profit_list
     2a-c: Visually, I'm thinking this will look something like: [(2ndElement=2ndMonthValue=y)-(1stElement=1stMonthValue=x)]
     2d. Then I want to store all the Profit/Losses between months in a new variable list (I'll call this list "res" for fun)
    3. Calculate average of res = [the list of changes in Profit/Losses between months over the entire period]
      3a. Calculate the count of the number of Profit/Losses in res
      3b. Calculate the sum of the Profit/Losses in res
      3c. Calculate the average change of Profit/Losses between months over the entire period
      3a-c. Visually, I'm thinking (3b/3a)=(sum(res)/count(res))=avg(3b)=mean(3b)
     4. Create a variable to store the average change of Profit/Losses between months over the entire period
    """
    #Approach 1, 2a-d Formula
    res = [y - x for x, y in zip(net_profit_list, net_profit_list[1:])]
        #print(net_profit_list)
        #print(net_profit_list[1:])
        #print(res)
    #Approach 3a-c
    import statistics
    #Approach 4
    x = statistics.mean(res)
    Average_Change = (f"Average  Change: ${round(x,2)}") #round(x,2) returns a rounded number to the second decimal point
#6a. Print (Average Change: $-2315.12)
    print(Average_Change)

#7. Calculate: The greatest increase in profits (date and amount) over the entire period
#8. Calculate: The greatest decrease in losses (date and amount) over the entire period

"""
Approach_Profits:
1. Identify the integer with the (max_value=highest value) in res = [the list of changes in Profit/Losses between months over the entire period]
2. Identify the integer with the (min_value=lowest value) in res = [the list of changes in Profit/Losses between months over the entire period]
3. Create a variable list to house only the csv 'Date' column values (minus the header)
*I think I could also delete the second row of csv 'Date' col as the month change begins with the second month
*this would change the formula I have slightly if I were to implement, but good to keep in mind
4. Join (or zip) the separate lists: zip(4aList+4bList)
4a.res = [the list of changes in Profit/Losses between months over the entire period] + 
4b. net_profit_plus_month = [the list of months in the 'Date' col minus header] 
4c. Pair the month value with the corresponding max_value or min_value
5. Identify each respective min/max value with the corresponding month 

"""
with open(csvpath, newline="") as csvfile: #Difficulty with return results (again); open file
    csvreader = csv.reader(csvfile, delimiter=",")
    #Approach_Profits 3
    net_profit_plus_month = [] #Create list variable to house csv 'Date' column
    for rows in csvreader:
        net_profit_plus_month.append(rows[0:1]) #Adds all months to list
    net_profit_plus_month.pop(0) #Remove the 'Date' header (approach #3)
    net_profit_plus_month_n = [i[0] for i in net_profit_plus_month] #Converts list to (string?) return "Jan 2016" instead of "('Jan 2016')" per value

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Approach_Profits 1 & 2
    max_value = max(res) #Max value of the Profit/Losses between months average list (res)
    min_value = min(res) #Min value of the Profit/Losses between months average list (res)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Approach_Profits 4
    result = [None]*(len(net_profit_plus_month_n)+len(res)) #"list by index": Assigns index #s to each list
    result[::2] = net_profit_plus_month_n #retain index order of each list; Profit/Losses match with month
    result[1::2] = res
    #Approach_Profits 5
    for x, y in zip(result, result[1:]): #Assign x to Profit/Losses; Assign y to month value
        if x == max_value: #If Profit/Loss matches with the determined max value
            Greatest_Increase = ("Greatest Increase in Profits: " + str(y) + " ("+str(x) +")")
        if x == min_value: #If Profit/Loss matches with the determined min value
            Greatest_Decrease = ("Greatest Decrease in Profits: " + str(y) + " ("+str(x) +")")
#7a. Print (Greatest Increase in Profits: Feb-2012 ($1926159))
            print(Greatest_Increase)
#8a. Print (Greatest Decrease in Profits: Sep-2013 ($-2196167))
            print(Greatest_Decrease)

print()
#9**. Your final script should both print the analysis to the terminal
#10**. Export a text file with the results
    #I ask the user if they'd like to create and export a text file of the results, just to be nice and polite and stuff.
Output_Text = input("Would you like to export a text file of the results? If yes, type 'y':")
if Output_Text == 'y':
    print("Okay, a text file of the results has been exported as 'pythonhw1-pybank-results-2018.txt'")
    f = open('pythonhw1-pybank-results-2018.txt','w')
    f.write(Financial_Analysis +  "\n" +
            Break_Lines +  "\n" +
            Total_Months +  "\n" +
            Total_Net +  "\n" +
            Average_Change +  "\n" +
            Greatest_Increase +  "\n" +
            Greatest_Decrease
            )
    f.close()
else:
    print("Okay, a text file of the results will *not* be exported :)")
