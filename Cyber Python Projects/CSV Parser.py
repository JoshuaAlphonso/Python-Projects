import csv

# Specify the file path and encoding
csv_file_path = "C:/Users/Python/Desktop/Logfile.CSV"
encoding = 'utf-8'  # or 'cp1252' or another appropriate encoding

# Open the CSV file with the specified encoding
with open(csv_file_path, mode='r', encoding=encoding) as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Process the row
        print(row)
