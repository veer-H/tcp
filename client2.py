import socket

# Server address and port (replace with actual EC2 instance IP)
HOST = "3.110.171.243"
PORT = 5000

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Receive uptime data
data = client_socket.recv(1024).decode()
print(data)

# Close the connection
client_socket.close()

print("Client disconnected")



