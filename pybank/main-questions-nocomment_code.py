#Final Questions
# 1. What is the fix for having to open the csv file more than once at outset?
# 2. How to close the csv file?
# 3. How to create a while loop at end so that if user says no, it loops back to the y/n question and the y response, so user
## won't have to re-run program to have the option if they decide (after selecton no first) to write to a text file the results?


import os
import csv

csvpath = os.path.join("budget_data.csv")

Financial_Analysis = ("Financial Analysis")
print(Financial_Analysis)
Break_Lines = ("--------------------------")
print(Break_Lines)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    next(csvfile)
    row_count = sum(1 for line in csvreader)
    Total_Months = ("Total Months: " + str(row_count))
    print(Total_Months)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    net_profit_list = []
    for rows in csvreader:
         net_profit_list.append(rows[1])
    net_profit_list.remove('Profit/Losses')
    net_profit_list = [int(rows) for rows in net_profit_list]
    total_net_value = str(sum(net_profit_list))
    Total_Net = (f"Total: ${total_net_value}")
    print(Total_Net)

        # Second approach that successfully calculates sum(net_profit_list)

        #def listsum(net_profit_list):
           # theSum = 0
            #for x in net_profit_list:
             #   theSum = theSum + x
           # return theSum
        #print(listsum(net_profit_list))


    res = [y - x for x, y in zip(net_profit_list, net_profit_list[1:])]
    import statistics
    x = statistics.mean(res)
    Average_Change = (f"Average  Change: ${round(x,2)}")
    print(Average_Change)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    net_profit_plus_month = []
    for rows in csvreader:
        net_profit_plus_month.append(rows[0:1])
    net_profit_plus_month.pop(0)
    net_profit_plus_month_n = [i[0] for i in net_profit_plus_month]

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    max_value = max(res)
    min_value = min(res)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    result = [None]*(len(net_profit_plus_month_n)+len(res))
    result[::2] = net_profit_plus_month_n
    result[1::2] = res
    for x, y in zip(result, result[1:]):
        if x == max_value:
            Greatest_Increase = ("Greatest Increase in Profits: " + str(y) + " ("+str(x) +")")
        if x == min_value:
            Greatest_Decrease = ("Greatest Decrease in Profits: " + str(y) + " ("+str(x) +")")
            print(Greatest_Increase)
            print(Greatest_Decrease)

print()

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