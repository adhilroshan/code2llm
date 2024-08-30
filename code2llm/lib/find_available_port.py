import socket

def find_available_port(start_port=2255, max_port=65535):
    """
    Find an available port starting from start_port.
    If start_port is not available, it increments and tries the next one.
    """
    for port in range(start_port, max_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Try to bind the socket to the port
            result = sock.connect_ex(('127.0.0.1', port))
            if result != 0:  # Port is available if connect_ex returns non-zero
                return port
    raise RuntimeError("No available ports found in the specified range.")
