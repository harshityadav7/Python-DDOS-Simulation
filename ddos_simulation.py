# ddos_simulation.py
import requests
import threading

# Target server details
url = "http://127.0.0.1:8080"  # Change this to your server's IP and port

# Function to send a request
def send_request():
    try:
        response = requests.get(url)
        print(f"Request sent: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Number of threads to simulate multiple requests
threads = []

# Simulate multiple clients by creating many threads
for i in range(100):  # You can increase this number to simulate more traffic
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
