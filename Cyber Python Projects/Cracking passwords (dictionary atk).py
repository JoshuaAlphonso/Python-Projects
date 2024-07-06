import hashlib

# Function to perform dictionary attack
def dictionary_attack(target_hash, password_file):
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == target_hash:
                return f"Password found: {password}"
    return "Password not found in the dictionary."

# Example usage
if __name__ == "__main__":
    # SHA-256 hash value to crack
    target_hash = input("Enter the SHA-256 hash value to crack: ")

    # Path to the password file containing candidate passwords
    password_file_path = input("Enter the path to the password file: ")

    # Perform the dictionary attack
    result = dictionary_attack(target_hash, password_file_path)
    print(result)

# C:\Users\Python\Desktop\Text.txt