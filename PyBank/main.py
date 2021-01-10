import os
import csv
import statistics

#set the initial values
net_total = 0
count = 0
this_row =0
next_row =0
change_dataset = []
greatest_increase = 0
greatest_decrease = 0

csvpath = os.path.join('.','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile) 
    csvheader = next(csvreader) #store header row and skip it for data counts
    for row in csvreader:
        count += 1  #number of rows after the header
        net_total += int(row[1])  #total of the profit/losses
        if count > 1: #start calculating the change with the second row
            next_row = row[1]
            change = int(next_row) - int(this_row) #cast as integers since they are initially strings
            change_dataset.append(change) #put all of the change values in a list to calc mean later
            if change > greatest_increase: #compare change in periods with greatest increase
                greatest_increase = change
                greatest_increase_per = row[0]
            if change < greatest_decrease: #compare change in periods with greatest decrease
                greatest_decrease = change
                greatest_decrease_per = row[0]
        this_row = row[1] #store the first row and then store the next row on the second loop to subtract them
        
average_change = round(statistics.mean(change_dataset),2) #use stats module to calc mean and round to 2 decimals

print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(count))
print("Total: $" + str(net_total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase_per) + " ($" + str(greatest_increase)+")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_per) + " ($" + str(greatest_decrease)+")")