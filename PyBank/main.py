#script for PyBank analysis

import os
import csv

#file reference to open and read csv file
pyBank_csv = os.path.join("Resources", "budget_data.csv").replace("\\","/")
    #added .replace due to error with os.path.join adding '\\' when referencing file
    #other option is to use direct path to reference file =  PyBank_csv = "Resources/budget_data.csv"

with open(pyBank_csv, newline='',encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
        #next skips header row

    #create Lists to store data
    date = []
    profit_loss = []
    amt_chg = []

    #add csv column to newly created lists
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])
        
    #loop through each row to calculate the change in profit_loss 
    i = 0
    while i < len(profit_loss): 
        if i == 0:
            amt_chg_value = 0
            amt_chg.append(amt_chg_value)
       
        else: 
            amt_chg_value = float(profit_loss[i]) - float(profit_loss[i-1]) 
            amt_chg.append(amt_chg_value)
        i += 1
    
    #Zip lists together
    cleaned_csv = zip(date, profit_loss, amt_chg)

#print outputs
    print("Financial Analysis")
    print("-------------------------------")
    
    #calc number of months
    print(f"Total Months: {len(date)}")
    
    #calc Total $s
    x = sum(map(int,profit_loss))
    print(f"Total: ${x}")

    #calc Average Change
    avg_chg = round(sum(map(int,amt_chg))/(len(amt_chg)-1),2)
    print(f"Average Change: ${str(avg_chg)}")       

    #calc Greatest Increase/Decrease in Profit
    max_chg = int(max(amt_chg))
    greatest_inc = 0
    min_chg = int(min(amt_chg))
    greatest_dec = 0

    for row in cleaned_csv:
        if row[2] == max_chg:
            greatest_inc = row[0]
            print (f"Greatest Increase in Profits: {greatest_inc} (${max_chg})")
    
        if row[2] == min_chg:
            greatest_dec = row[0]
            print (f"Greatest Decrease in Profits: {greatest_dec} (${min_chg})")

#Set variable for output file
file = open("PyBank_analysis.txt",'w')
file.writelines(["\nFinancial Analysis","\n-------------------------------"])
file.writelines(f"\nTotal Months: {str(len(date))}")
file.writelines(f"\nTotal: ${x}")
file.writelines(f"\nAverage Change: ${str(avg_chg)}")
file.writelines(f"\nGreatest Increase in Profits: {greatest_inc} (${max_chg})")
file.writelines(f"\nGreatest Decrease in Profits: {greatest_dec} (${min_chg})")





