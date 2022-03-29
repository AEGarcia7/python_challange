import os
import csv
from statistics import mean

csvpath = os.path.join('Resources','budget_data.csv')

months = []
total = []
change = []
avchange = []
newmonth = []
newtotal = []
newave = []
highave = []
lowave = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') 

    csv_header = next(csvreader)
    

    for row in csvreader:
        
        months.append(row[0])

        total.append(row[1])


    print("Financial Analysis")

    print("------------------------------------")

    print("Total Months:", len(months))

    total_money = [int(i) for i in total]

    print("Total: $", sum(total_money))

    change = [total_money[m+1] - total_money[m] for m in range(len(total_money)-1)]

    avchange = round(mean(change),2)

    print("Average Change:", avchange)

    new_chart = zip(months, total_money, change)

    for line in new_chart:

        newave.append(line[2])

    highave = max(newave)
    
    highmonthindex = newave.index(highave)

    truehighmonthindex = highmonthindex+1
 
    print("Greatest Increase in Profits: ", (months[truehighmonthindex]),highave)

    lowave = min(newave)

    lowmonthindex = newave.index(lowave)

    truelowmonthindex = lowmonthindex+1    

    print("Greatest Decrease in Profits:", (months[truelowmonthindex]),lowave)

    output_path = os.path.join("Analysis","Financial Analysis.txt")

    with open(output_path, 'w') as csvfile:

        csvwriter = csv.writer(csvfile,delimiter='|')

        csvwriter.writerow(["Financial Analysis"])

        csvwriter.writerow(["------------------------------------"])
        
        csvwriter.writerow(["Total Months:",len(months)])

        csvwriter.writerow(["Total: $",sum(total_money)])

        csvwriter.writerow(["Average Change:",avchange])

        csvwriter.writerow(["Greatest Increase in Profits: ",(months[truehighmonthindex]),highave])

        csvwriter.writerow(["Greatest Decrease in Profits:",(months[truelowmonthindex]),lowave])