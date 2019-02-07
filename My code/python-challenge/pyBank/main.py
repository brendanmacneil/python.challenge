#Import Dependencies.
import os, csv
from pathlib import Path 

#Declare file location via pathlib.
input_file = Path("python-challenge", "pyBank", "budget_data.csv")

#Create empty lists to iterate through specific rows for the following variables.
total_months = []
total_profit = []
monthly_profit_change = []
 
#Open csv.
with open(input_file,newline="", encoding="utf-8") as budget:

     #Store contents of file in the variable csvreader.
    csvreader = csv.reader(budget,delimiter=",") 

    #Skip over header labels.
    header = next(csvreader)  

    #Go through the rows in the contents of the stored file.
    for row in csvreader: 

        #APPEND the total months and total profit to their corresponding lists.
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Go through the profits in order to get the monthly change in profits.
    for i in range(len(total_profit)-1):
        
        #Take the difference between two months and APPEND to MONTHLY PROFIT CHANGE.
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
#Get the max and min of the the MONTHLY PROFIT CHANGE list.
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

#Get maximum and minimum values to the correct month using the list and index from max and min.
#Use the plus 1 at the end since month associated with change is the + 1 month or next month.
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#Print information.

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#output file
output_file = Path("python-challenge", "pyBank", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
#Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
