# Dependencies
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')
budget_text_analysis = os.path.join("analysis", "budget_analysis.txt")

# First - find total months and net profit
total_months = 0
net_profit = 0

# Must establish staring points
starting_profit = 0

# Second - Find monthly change
current_month_change = 0
average_change = 0

# Third - find the greatest decrease and greatest increase based on monthly changes
greatest_decrease = ["", 0]
greatest_increase = ["", 0]

net_change_values = []
monthly_change = []


# Read in the CSV file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    # Extract the first title row and start reading data from second row
    title_row = next(csvreader)

    # Change second row values to integers
    net_profit += int(title_row[1])
    starting_profit = int(title_row[1])
    total_months += 1

    for row in csvreader:
        # Total number of months included in the dataset
        total_months += 1

        # The net total amount of "Profit/Losses" over the entire period
        net_profit += int(row[1])

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        net_changes = int(row[1]) - starting_profit
        starting_profit = int(row[1])
        net_change_values += [net_changes]
        monthly_change += [row[0]]
        
        # The greatest decrease in profits (date and amount) over the entire period

        if greatest_decrease[1] > net_changes:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_changes

        # The greatest increase in profits (date and amount) over the entire period
        if greatest_increase[1] < net_changes:
                greatest_increase[0] = row[0]
                greatest_increase[1] = net_changes

        
average_change = round(sum(net_change_values)/len(net_change_values),2)

# Format the analysis that can be put into a file
budget_analysis = (
     f"Financial Analysis\n\n" 
     f"----------------------------\n"
     f"Total Months: {total_months}\n\n"
     f"Total: ${net_profit}\n\n"
     f"Average Change: ${average_change}\n\n"
     f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n\n"
     f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)
print(budget_analysis)

# Write the budget analysis into a file into budget_text_analysis
with open(budget_text_analysis, "w") as file:
    file.write(budget_analysis)




