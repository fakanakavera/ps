import socket

class RaspConnection:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((RASP_HOST, RASP_PORT))
        self.sock = setSocket()

    def send_action(self, action):
        self.sock.send(str.encode(str(action)))

    def send_fast_fold(self):
        self.send_action('99')

