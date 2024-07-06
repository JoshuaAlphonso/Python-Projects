import csv

# Specify the file path and encoding
csv_file_path = "C:/Users/Python/Desktop/Logfile.CSV"
encoding = 'utf-8'  # or 'cp1252' or another appropriate encoding

# Define the word to search for
search_word = "adware"

# Open the CSV file with the specified encoding
with open(csv_file_path, mode='r', encoding=encoding) as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Iterate over each cell in the row
        for cell in row:
            # Check if the search word is in the current cell
            if search_word in cell:
                # Process the row if the word is found
                print(row)
                # Exit the loop to avoid printing duplicate rows
                break
