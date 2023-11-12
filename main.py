from connectivity.socket_connection import SocketConnection
from processing.twitter_procesor import TwitterProcessor
import time


if __name__ == '__main__':
    """
    Entry point of the program. Collect data in the socket and execute the apache beam data pipeline every 20 seconds.
    """
    host = "localhost"
    port = 5555
    socket = SocketConnection(host, port)

    # Close the connection in case of error and raise an exception.
    try:
        while True:
            time.sleep(20)
            data = socket.get_data()
            data = data.decode("utf-8")
            TwitterProcessor.run([data])
    except:
        raise
    finally:
        socket.close()
