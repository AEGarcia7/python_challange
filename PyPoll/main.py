import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

ballot_id = []
county = []
candidate = []
totalvotes = 0
charles = []
charlespercent = 0
diana = []
dianapercent = 0
raymon = []
raymonpercent = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') 

    csv_header = next(csvreader)

    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    print("Election Results")

    print("-----------------------------")

    totalvotes = len(ballot_id)

    print("Total Votes:", totalvotes)

    print("-----------------------------")

    charles = candidate.count('Charles Casper Stockham')

    charlespercent = (charles/totalvotes)*100

    print("Charles Casper Stockham: %",round(charlespercent,3),charles)

    diana = candidate.count('Diana DeGette')

    dianapercent = (diana/totalvotes)*100

    print("DianaDeGette: %", round(dianapercent,3),diana)

    raymon = candidate.count('Raymon Anthony Doane')

    raymonpercent = (raymon/totalvotes)*100

    print("Raymon Anthony Doane: %", round(raymonpercent,3),raymon)

    print("-----------------------------")

    if charlespercent > dianapercent and raymonpercent:
        print("Winner: Charles Casper Stockham")

    elif dianapercent > charlespercent and raymonpercent:
        print("Winner: Diana DeGette")

    else:
        print("Winner: Raymon Anthony Doane")

    print("-----------------------------")

    output_path = os.path.join("Analysis","Election Results.txt")

    with open(output_path, 'w') as csvfile:

        csvwriter = csv.writer(csvfile,delimiter='|')

        csvwriter.writerow(["Election Results"])

        csvwriter.writerow(["-----------------------------"])

        csvwriter.writerow(["Total Votes:", totalvotes])

        csvwriter.writerow(["-----------------------------"])

        csvwriter.writerow(["Charles Casper Stockham: %",round(charlespercent,3),charles])

        csvwriter.writerow(["DianaDeGette: %", round(dianapercent,3),diana])

        csvwriter.writerow(["Raymon Anthony Doane: %", round(raymonpercent,3),raymon])

        csvwriter.writerow(["-----------------------------"])

        csvwriter.writerow(["Winner: Diana DeGette"])

        csvwriter.writerow(["-----------------------------"])