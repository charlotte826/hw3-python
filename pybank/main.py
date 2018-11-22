
#Instruction: Analyze the financial records of your company, contained in set of financial data called budget_data.csv

#The OS module in Python provides a way of using operating system dependent functionality.
import os
import csv

#Import csv working file: budget_data.csv
#csv file in quotes because file is copied to same folder that contains main.py (current file)
csvpath = os.path.join("budget_data.csv")


#Note: Ensure all lines within a "with open" are indented so that they perform within the open file. otherwise the file will close
print("Financial Analysis")
print("--------------------------")
#Open and read the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #print(csvreader)

#Instruction: Calculate the total number of months included in the dataset
#Create code to count lines because each line in csv signifies a month
    next(csvfile) #skip the header row of csv file
    row_count = sum(1 for line in csvreader)
    #Instruction: Print "Total Months: 86"
    print("Total Months: " + str(row_count))

#Instruction: Calculate the total net amount of "Profit/Losses" over the entire period
     #Formulate code that will allow us to add all values in column Profit/Losses to calculate total net amount
     #The dataset is composed of two columns: Date and Profit/Losses

#Approach 1 as of Study Group 11.21.18
    # Make a list of the values in the second column and then add them together
    # Elements: For loop. Create list(s). Append values to list(s).
    #Create two empty lists
# for loop through sheet.

#Here I see list elements numbers as string)
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    month = []
    net_profit_list = []
    net_profit_list = [int(i) for i in net_profit_list]
    #net_profit_int = net_profit_list(map(int, net_profit_int))
    for rows in csvreader:
         net_profit_list.append(rows[1])
    #print(net_profit_list)
    net_profit_list.remove('Profit/Losses')
    #print(net_profit_list)
    net_profit_list = [int(rows) for rows in net_profit_list]
    #print(net_profit_list)
    #print(sum(net_profit_list))

#Print "Total: $38382578"
    print("Total: $" + str(sum(net_profit_list)))

#Loop through both rows to calculate average change in Profit/Losses between months over the entire period
    #avg_change = (amount of last row - amount of first row / total length - 1)
    #totalNetAmount = 0
    #total_months = total_months + 1
    #from statistics import mean
    #for first, second in zip(net_profit_list, net_profit_list[1:]):
    #zip(*[iter(net_profit_list)] * 2)
    #x = [net_profit_list(t) for t in zip(*[iter(range(1, 87))] * 2)]
    #print(x)
    zip(*[iter(net_profit_list)]*2)
    print(net_profit_list)

    #from statistics import mean
    #mean(net_profit_list)
    #print(mean(net_profit_list))

    for first, second in zip(net_profit_list, net_profit_list[1:]):
        print(sum(first, second) / float(len(first, second)))

        #Print "Average Change: $-2315.12"

#Loop through rows in both columns to calculate the greatest increase in profits (date and amount) over entire period

#Print "Greatest Increase in Profits: Feb-2012 ($1926159)"

#Loop through rows in both columns to calculate the greatest decrease in losses (date and amount) over the entire period

#Print "Greatest Decrease in Profits: Sep-2013 ($-2196167)"

#Print entire analysis to terminal

#Export a text file with the results


