# Import the csv module
import csv

# Open the CSV file
with open("data.csv") as f:
    # Read the CSV data
    data = csv.reader(f)

    # Loop through each row in the CSV data
    for row in data:
        # Get the values from column 1 and column 2
        col1, col2 = row

        # Print the values from column 1 and column 2
        print("Column 1:", col1)
        print("Column 2:", col2)

##############Output Looks Like this 

###   value1,value2
###   value3,value4
###   value5,value6

