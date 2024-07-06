def search_word_in_log(log_file_path, search_word):
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if search_word in line:
                    print(line.strip())
    except FileNotFoundError:
        print("File not found.")

# Replace 'emails.log' with the path to your .log file
log_file_path = 'C:\\Users\\Python\\Desktop\\apache-ex2.log'
search_word = 'HTTP'  # Replace 'error' with the word you want to search for
search_word_in_log(log_file_path, search_word)
