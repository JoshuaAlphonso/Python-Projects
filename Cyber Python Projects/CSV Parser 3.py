import csv

def search_csv(file_path, search_word):
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if search_word in row:
                    print(row)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = "example.csv"
search_word = "specific_word"
search_csv(file_path, search_word)
