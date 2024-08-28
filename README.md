# Python-DDOS-Simulation

Python DDoS Simulation
This project demonstrates how to create a simple Python HTTP server and simulate a Distributed Denial of Service (DDoS) attack for educational purposes. 


# Features
Simple Python HTTP server using http.server
DDoS simulation script to generate high traffic loads
Log file generation to monitor incoming requests
Getting Started

# Prerequisites
Python 3.x
requests module (for DDoS simulation)

# Installation
Clone this repository:

git clone https://github.com/harshityadav7/Python-DDOS-Simulation.git
cd python-ddos-simulation

# Usage
1. Start the Server
To start the Python HTTP server:

bash 
python server.py

The server will start listening on all available interfaces at port 8080. It will log incoming requests to server.log.

2. Simulate a DDoS Attack
To simulate a DDoS attack against the server:

bash
python ddos_simulation.py

This script will create multiple threads, each sending requests to the server to simulate a DDoS attack.

Logs
All incoming requests to the server are logged in server.log.
Disclaimer
This project is for educational purposes only. DDoS attacks can cause significant harm and are illegal when performed without authorization. Always ensure you are in a controlled and legal environment when using this code.

Contributing
Feel free to submit issues or pull requests if you have suggestions for improving this project.
