import socket
import csv

# Server address and port
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5000
# Path to the uptime data file (modify as needed)
DATA_FILE_PATH = "/home/ubuntu/uptime_data.tsv"
# Open the uptime data file

data = []
with open(DATA_FILE_PATH, 'r') as file:
    for line in file:
      # Split the line based on the tab delimiter
      data.append(line.strip().split('\t'))


# Example usage


# Access data
# Access the timestamp and uptime elements
timestamp, uptime = data[1]

# Concatenate the formatted string
output_string = "Timestamp: " + timestamp + ", Uptime: " + uptime

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print("Server started listening on port", PORT)

# Accept a new connection
client_socket, address = server_socket.accept()
print("Client connected from", address)

# Send uptime data
client_socket.sendall(output_string.encode())

# Close the connection
client_socket.close()
server_socket.close()

print("Server stopped")
