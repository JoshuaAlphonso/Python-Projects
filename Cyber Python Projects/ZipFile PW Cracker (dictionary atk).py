import zipfile

def extract(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except Exception as e:
        return False

def main():
    file_path = input("Enter the path to the file: ")
    dict_path = input("Enter the path to the dictionary: ")

    with zipfile.ZipFile(file_path) as zip_file:
        with open(dict_path, 'r') as dictionary:
            for line in dictionary:
                password = line.strip()
                if extract(zip_file, password):
                    print(f"Password found: {password}")
                    return

    print("Password not found.")

if __name__ == "__main__":
    main()
