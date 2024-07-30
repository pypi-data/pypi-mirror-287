#   pyZink > connect > tcp.py
#   morten@znk.dk
#   Created April 2024
"""
    This document contains functionality to make a simple TCP client/server used for diagnostics
"""

import socket

def tcp_server(server_port: int, server_ip: str = "localhost") -> None:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((server_ip, server_port))
        sock.listen(1)
        print(f"INFO: Started TCP-server on {server_ip}:{server_port}")
        
        while True:
            conn, addr = sock.accept()
            print(f"Connected with {addr[0]} on port {addr[1]}")
            conn.close()
    except KeyboardInterrupt:
        print("WARNING: Socket closed with keyboard interrupt")
    finally:
        sock.close()

def tcp_client(server_ip: str, server_port: int) -> None:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"INFO: Client started. Attempting to connect to server on {server_ip}:{server_port}")
        sock.connect((server_ip, server_port))
        print(f"INFO: Successfully sonnected to server on {server_ip}:{server_port}")
    finally:
        sock.close()
        print("WARNING: Socket closed")

if __name__ == "__main__":
    import threading

    thread = threading.Timer(5, tcp_client, args=("localhost", 12345))
    thread.start()

    tcp_server(12345)