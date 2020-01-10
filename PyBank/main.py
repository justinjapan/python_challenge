
import csv
import os
import statistics


#Create list to iterate through specific rows for the following 
Month_Count = []
Profit_amount = []
Monthly_change = []

#Open csv file in read

with open("budget_data.csv", "r") as pybank:
	reader = csv.reader(pybank)
	
#skip first row to remove the headers 	

	next(reader)

#create a loop that creates two list. This will allow you to manipulate the data 	

	for row in reader:
		Month_Count.append(row[0])
		Profit_amount.append(int(row[1]))
		
#Loop through profit list to get difference in each month
		
for i in range(len(Profit_amount)-1):
	
	#Take the difference between two months and append it to monthly change
        
		Monthly_change.append(Profit_amount[i+1]-Profit_amount[i])
		
#establish min and max values from the profit list

best_increase = max(Monthly_change)
best_decrease = min(Monthly_change)

#Connect max and min using month list and index / use +1 to associate the change to the next coming month
best_increase_month = Monthly_change.index(max(Monthly_change)) + 1
best_decrease_month = Monthly_change.index(min(Monthly_change)) + 1

#Print Statements


print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {len(Month_Count)}")
print(f"Total: ${sum(Profit_amount)}")
print(f"Average Change: {round(sum(Monthly_change)/len(Monthly_change),2)}")
print(f"Greatest Increase in Profits: {Month_Count[best_increase_month]} (${(str(best_increase))})")
print(f"Greatest Decrease in Profits: {Month_Count[best_decrease_month]} (${(str(best_decrease))})")


#Create a text file to print the Analysis of PyBank


with open("pybank_work", "w") as file:

#Write analysis data to file using \n in order to write each line one below the other

	file.write("Financial Analysis")
	file.write("\n")
	file.write("----------------------------------------------------")
	file.write("\n")
	file.write(f"Total Months: {len(Month_Count)}")
	file.write("\n")
	file.write(f"Total: ${sum(Profit_amount)}")
	file.write("\n")
	file.write(f"Average Change: {round(sum(Monthly_change)/len(Monthly_change),2)}")
	file.write("\n")
	file.write(f"Greatest Increase in Profits: {Month_Count[best_increase_month]} (${(str(best_increase))})")
	file.write("\n")
	file.write(f"Greatest Decrease in Profits: {Month_Count[best_decrease_month]} (${(str(best_decrease))})")
	
	
