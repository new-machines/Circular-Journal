import csv
import datetime

# Get user input
user_input = input("Enter a paragraph: ")

# Get the current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create or open the CSV file for writing
with open('entries.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the user input and timestamp to the CSV file
    writer.writerow([timestamp, user_input])

print("Data has been written to entries.csv with timestamp.")