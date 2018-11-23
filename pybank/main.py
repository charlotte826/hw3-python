
#Instruction: Analyze the financial records of your company, contained in set of financial data called budget_data.csv

#The OS module in Python provides a way of using operating system dependent functionality.
import os
import csv

#Import csv working file: budget_data.csv
#csv file in quotes because file is copied to same folder that contains main.py (current file)
csvpath = os.path.join("budget_data.csv")


#Note: Ensure all lines within a "with open" are indented so that they perform within the open file. otherwise the file will close
#Create a variable to hold the phrase
Financial_Analysis = ("Financial Analysis")
print(Financial_Analysis)
#Create a variable to hold the divider
Break_Lines = ("--------------------------")
print(Break_Lines)

#Open and read the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #print(csvreader)

#Instruction: Calculate the total number of months included in the dataset
#Create code to count lines of csv because each line in csv signifies a month
    next(csvfile) #skip count of the header row of csv file
    row_count = sum(1 for line in csvreader)
    #Instruction: Print "Total Months: 86"
    #Create variable to hold months result
    Total_Months = ("Total Months: " + str(row_count))
    print(Total_Months)

#Instruction: Calculate the total net amount of "Profit/Losses" over the entire period
     #Formulate code that will allow us to add all values in csv column Profit/Losses to calculate total net amount
     #The dataset is composed of two columns: Date and Profit/Losses

#Approach 2: Charlotte 11.21.18
#Having trouble getting this to return results, so I opened the file again and it started working. Could be an indentation/block issue.
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Create variable list to hold 'Profit/Losses' values
    net_profit_list = []
    #net_profit_list = [int(i) for i in net_profit_list]
    #net_profit_int = net_profit_list(map(int, net_profit_int))
    #Create for loop through csv to add only the 'Profit/Losses' column values of csv into the list
    for rows in csvreader:
         net_profit_list.append(rows[1])
    #print(net_profit_list)
    #Remove the header -- can also use pop to remove 1st element (which is header) -- as seen done on another list further along in code
    net_profit_list.remove('Profit/Losses')
    #print(net_profit_list)
    #Convert list elements into integers
    net_profit_list = [int(rows) for rows in net_profit_list]
    #print(net_profit_list)
    #print(sum(net_profit_list))

#Print "Total: $38382578"
    #Create variable to house sum of Net Profit and result
    Total_Net = ("Total: $" + str(sum(net_profit_list)))
    print(Total_Net)


 # Another approach I wrote which calculates the sum of net_profit_list

    #def listsum(net_profit_list):
       # theSum = 0
        #for x in net_profit_list:
         #   theSum = theSum + x
       # return theSum
    #print(listsum(net_profit_list))

#Instructions: Find the average change in "Profit/Losses" between months over the entire period
    """
    Approach
    1. I want to create a formula to find the average change in Profit/Losses between months over the entire period. 
    2. To find the average change, I will want to:
     2a. subtract the second element in the list from the first element
     2b. subtract the third element from the second element 
     2c. and so forth, continuing this pattern, iterating over the entire list of net_profit_list
     2d. Then I want to store all the "between month" sums together (which will be the net values between each month) in a variable (res)
    3. To find the average of this new variable (res)
      3a. the count of the number of "between month" sums
      3b. the new total net sum of all "between month" sums
      3c. the average of the new total net sum
     4. I want to create a variable to store the average of the new total net sum, which will represent the 
        average change in Profit/Losses between months
    """
#Approach 1. Formula for average change in Profit/Losses between months over entire period
#Approach 2a-d
    res = [y - x for x, y in zip(net_profit_list, net_profit_list[1:])]
    #print(res)
#Approach 3a-c
    import statistics

#Approach 4
    x = statistics.mean(res)
    #round(x,2) returns a rounded number to the second decimal point
    Average_Change = (f"Average  Change: ${round(x,2)}")
    print(Average_Change)

#Instructions: Find 1. Greatest Increase in Profits: Feb-2012 ($1926159)
#and find 2. Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""
Approach_Profits:
1. I want to identify the integer with the highest value in the between-month-net list
2. I want to identify the integer with the lowest value in the between-month-net list
3. I want to create a variable list and house only the months column, minus the header (I think I could also delete the second row, too, as the 
month change begins with the second month -- this would change the formula I have slightly, but good to keep in mind)
4. I want to combine the separate lists (between-month-net = res) and (months = net_profit_plus_month) so I can create a formula to pair the month with
the corresponding net-value
5. I want to identify with each respective value the corresponding month 

"""
#Having trouble getting this to return results (again), so I opened the file again and it started working. Could be an indentation/block issue.
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#Approach_Profits 3
    #Create variable to house csv Date column in a separate list from Profit/Losses list
    net_profit_plus_month = []
    for rows in csvreader:
        net_profit_plus_month.append(rows[0:1]) #Adds all months to list
    #Remove header "Date"
    net_profit_plus_month.pop(0)
    #Converts list to return Jan 2016 instead of ('Jan 2016') per value
    net_profit_plus_month_n = [i[0] for i in net_profit_plus_month]
    #print(net_profit_plus_month_n)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#Approach_Profits 1 & 2
    #Returns the maximum value of the Profit/Losses between months average list (res)
    max_value = max(res)
    #print(max_value)
    #Returns the minimum value of the Profit/Losses between months average list (res)
    min_value = min(res)
    #avg_value = sum(res) / len(res)
    #print(min_value)
    #print(avg_value)

#Concatonates both lists with 1 list first then 2 list second
#with open(csvpath, newline="") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #list_month_avg = net_profit_plus_month + net_profit_list
    #print(list_month_avg)

#Having trouble getting this to return results (again), so I opened the file again and it started working. Could be an indentation/block issue.
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#Approach_Profits 4
    result = [None]*(len(net_profit_plus_month_n)+len(res))
    result[::2] = net_profit_plus_month_n
    result[1::2] = res
    #print(result)
#Approach_Profits 5
    for x, y in zip(result, result[1:]):
        if x == max_value:
            Greatest_Increase = ("Greatest Increase in Profits: " + str(y) + " ("+str(x) +")")
        if x == min_value:
            Greatest_Decrease = ("Greatest Decrease in Profits: " + str(y) + " ("+str(x) +")")
            print(Greatest_Increase)
            print(Greatest_Decrease)

print()
#Instruction: your final script should both print the analysis to the terminal and export a text file with the results.
#I ask the user if they'd like to create and export a text file of the results, just to be nice and polite and stuff.
Output_Text = input("Would you like to export a text file of the results? If yes, type 'y':")
if Output_Text == 'y':
    f = open('pythonhw1-results-2018.txt','w')
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
    print("Okay, a text file of the results will not be exported :)")