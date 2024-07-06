import socket

def scan_port(target_host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        # Attempt to connect to the target host and port
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        # Close the socket
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {str(e)}")

def main():
    # Get the target host and port range from the user
    target_host = input("Enter the target host IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    # Scan each port in the specified range
    print(f"Scanning ports {start_port} to {end_port} on {target_host}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(target_host, port)

if __name__ == "__main__":
    main()
