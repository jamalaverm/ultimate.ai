import socket


class SocketConnection:
    """
    Establish a connection with the socket with the streaming data.
    """
    def __init__(self, host, port):
        """
        Constructor of the class.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def get_data(self, size=8192):
        """
        Get data from the socked, the buffer size is specified.
        """
        data = self.socket.recv(size)
        return data

    def close(self):
        """
        Close the connection with the socket.
        """
        self.socket.close()
