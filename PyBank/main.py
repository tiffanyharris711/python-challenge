import os
import csv

#set the initial values
net_total = 0
count = 0

csvpath = os.path.join('/Users','tiffanyharris','Desktop','git_things','myGitRepos','python-challenge','PyBank','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile) #Use DictReader instead of reader to skip header
    for row in csvreader:
        count += 1  #number of rows after the header
        net_total += int(row["Profit/Losses"])  #total of the profit/losses

print("Total Months: " + str(count))
print("Total: $" + str(net_total))
