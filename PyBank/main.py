import os
import csv

csv_path = os.path.join('../..', 'UCIRV201807DATA4-Class-Repository-DATA/02-Homework/03-Python/'
                                 'Instructions/PyBank/Resources/budget_data.csv')

with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # parse out header
    next(csv_reader)

    # add month-year column and profit/loss column into their own lists
    months_list = []
    change_list = []
    for row in csv_reader:
        months_list.append(row[0])
        change_list.append(int(row[1]))

total_net_amount = sum(i for i in change_list)

# list of the change in profit between months
monthly_change = []
for i in range(len(change_list)):
    if (i - 1) < 0:
        monthly_change.append(0)
    else:
        monthly_change.append(change_list[i] - change_list[i - 1])

# counting the number of months that have a change in value
count_of_monthly_changes = sum(1 for x in monthly_change if x != 0)

#
average_change = round(sum(monthly_change)/count_of_monthly_changes, 2)

# index of the max/min profit change
max_change = max(monthly_change)
min_change = min(monthly_change)
max_change_index = monthly_change.index(max_change)
min_change_index = monthly_change.index(min_change)

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(months_list)}')
print(f'Total: $ {total_net_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits {months_list[max_change_index]} (${max_change})')
print(f'Greatest Decrease in Profits {months_list[min_change_index]} (${min_change})')

output_path = os.path.join('main.csv')

with open(output_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['Financial Analysis'])
    csv_writer.writerow(['----------------------------'])
    csv_writer.writerow(['Total Months:', f'{len(months_list)}'])
    csv_writer.writerow(['Total:', f'${total_net_amount}'])
    csv_writer.writerow(['Average Change:', f'${average_change}'])
    csv_writer.writerow(['Greatest Increase in Profits:', f'{months_list[max_change_index]}', f'${max_change}'])
    csv_writer.writerow(['Greatest Decrease in Profits:', f'{months_list[min_change_index]}', f'${min_change}'])
