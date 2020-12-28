import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
total_profitLoss = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    lines = len(list(csvreader))
    print("Total Months: " + str(lines-1))
    for row in csvreader:
        profit_loss = row[1]
        total_profitLoss = profit_loss + total_profitLoss
    print(total_profitLoss)
