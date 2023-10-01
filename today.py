import csv
import datetime

# Get the current month and day as strings
current_month = datetime.datetime.now().strftime("%m")
current_day = datetime.datetime.now().strftime("%d")

# Create a list to store matching entries
matching_entries = []

# Read the entries from the CSV file and collect matching entries
with open('entries.csv', mode='r') as file:
    reader = csv.reader(file)
    
    # Loop through the rows in the CSV file
    for row in reader:
        timestamp = row[0]
        entry_text = row[1]
        
        # Parse the timestamp to get the year, month, and day
        entry_date = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        entry_year = entry_date.strftime("%Y")
        entry_month = entry_date.strftime("%m")
        entry_day = entry_date.strftime("%d")
        
        # Check if the month and day match the current date
        if entry_month == current_month and entry_day == current_day:
            matching_entries.append((entry_year, entry_text))

# Sort the matching_entries list in descending order of the year
matching_entries.sort(key=lambda x: x[0], reverse=True)

# Print the message for matching entries
print(f"All entries for this date, {current_month}-{current_day}:")

# Print each matching entry with just its year
for entry_year, entry_text in matching_entries:
    print(f"Year: {entry_year}, Entry: {entry_text}")
