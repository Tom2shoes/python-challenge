import os
import csv

csv_path = os.path.join('../..', 'UCIRV201807DATA4-Class-Repository-DATA/02-Homework/03-Python/'
                                 'Instructions/PyBank/Resources/budget_data.csv')

with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # parse out header
    next(csv_reader)

    # add month-year column profit/loss column into their own lists
    # Should this be a dictionary?
    months_list = []
    change_list = []
    for row in csv_reader:
        months_list.append(row[0])
        change_list.append(int(row[1]))

total_net_amount = sum(i for i in change_list)

average_change = total_net_amount/len(change_list)

max_change_index = change_list.index(max(change_list))
min_change_index = change_list.index(min(change_list))

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(len(months_list)))
print('Total: $' + str(total_net_amount))
print('Average Change: $' + str(round(average_change, 2)))
print('Greatest Increase in Profits: ' + months_list[max_change_index] +
      ' ($' + str(max(change_list)) + ')')
print('Greatest Decrease in Profits: ' + months_list[min_change_index] +
      ' ($' + str(min(change_list)) + ')')


