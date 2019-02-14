import csv
import os

total = []
change = []
greatincrease = 0
greatdecrease = 0

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    count = 0
    next(csvreader)
    for row in csvreader:
        count = count + 1
        total.append(int(row[1]))
        if int(row[1]) > greatincrease:
            greatincrease = int(row[1])
            increasedate = row[0]
        if int(row[1]) < greatdecrease:
            greatdecrease = int(row[1])
            decreasedate = row[0]
        for i in range(len(total)-1):
            change.append(total[i+1] - total[i])

    profit = sum(total)
    ave = round(sum(change) / float(len(change)), 2)


    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months: {count}')
    print(f'Total: ${profit}')
    print(f'Average Change: ${ave}')
    print(f'Greatest Increase in Profits: {increasedate} (${greatincrease})')
    print(f'Greatest Decrease in Profits: {decreasedate} (${greatdecrease})')
    print("---------------------------")
    print(f"Over the course of the past {count} months, our company has totaled ${profit} in profit.")
    print(f'Our average profit/loss per month was a loss of {ave}. I conclude that the average was negative,')
    print(f'but our net was positive due to several months with large losses, principally due to August 2012, September 2013,')
    print(f'February 2016, and July 2016.')


output_file = os.path.join("PyBank_Results.txt")
with open(output_file, "w") as txtfile:
     txtfile.write("Financial Analysis" + "\n")
     txtfile.write("---------------------------" + "\n")
     txtfile.write("Total Months: " + str(count) + "\n")
     txtfile.write("Total: " + "$" + str(profit) + "\n")
     txtfile.write("Average Change: " "$" + str(ave) + "\n")
     txtfile.write("Greatest Increase in Profits: " + str(increasedate) + " (" + "$" + str(greatincrease) + ")" + "\n")
     txtfile.write("Greatest Decrease in Profits: " + str(decreasedate) + " (" + "$" + str(greatdecrease) + ")" +  "\n")
     txtfile.write("---------------------------" + "\n")
     txtfile.write("Over the course of the past " + str(count) + " months, our company has totaled " + str(profit) + "in profit." + "\n")
     txtfile.write('Our average profit/loss per month was a loss of ' + str(ave) + '. I conclude that the average was negative,' + "\n")
     txtfile.write('but our net was positive due to several months with large losses, principally due to August 2012, September 2013,' + "\n")
     txtfile.write('February 2016, and July 2016.' + "\n")
     txtfile.close()
