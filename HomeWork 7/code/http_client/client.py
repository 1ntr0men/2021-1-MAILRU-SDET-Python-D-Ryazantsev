import socket
import json
import settings


class Client:

    def __init__(self):
        self.host = settings.MOCK_HOST
        self.port = int(settings.MOCK_PORT)
        self.url = f'http://{self.host}:{self.port}'
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        # client.connect((self.host, self.port))
        self.client = client

        self.logger = open('/tmp/logger.log', 'a')

    def connect(self):
        try:
            self.client.connect((self.host, self.port))
        except:
            pass

    def _data(self):
        total_data = []
        while True:
            self.connect()
            try:
                data = self.client.recv(4096)
            except:
                self.connect()
                data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        data = "".join(total_data).splitlines()
        self.logger.write(str(data) + "\n\n")
        self.logger.write("-" * 50 + "\n\n")
        return data

    def add_user(self, name, surname):

        j = json.dumps({"name": name, "surname": surname})
        request = f"POST /add_user HTTP/1.0\r\n" \
                  f"Host:{self.host}\r\n" \
                  f"Content-type: application/json\r\n" \
                  f"Content-Length: {len(j)}\r\n\r\n" \
                  f"{j}\r\n"
        self.logger.write(request)
        self.connect()
        self.client.send(request.encode())

        return self._data()

    def get_user(self, name):

        params = f'/get_user/{name}'
        request = f'GET {params} HTTP/1.0\r\n' \
                  f'Host:{self.host}\r\n\r\n'
        self.logger.write(request)
        self.connect()
        self.client.send(request.encode())

        return self._data()

    def delete_user(self, name):

        params = f'/delete_user/{name}'
        request = f'DELETE {params} HTTP/1.0\r\n' \
                  f'Host:{self.host}\r\n\r\n'
        self.logger.write(request)
        self.connect()
        self.client.send(request.encode())

        return self._data()

    def put_user(self, name, surname):
        j = json.dumps({"name": name, "surname": surname})
        request = f"PUT /update_surname HTTP/1.0\r\n" \
                  f"Host:{self.host}\r\n" \
                  f"Content-type: application/json\r\n" \
                  f"Content-Length: {len(j)}\r\n\r\n" \
                  f"{j}\r\n"
        self.logger.write(request)

        self.connect()
        self.client.send(request.encode())

        return self._data()

    def close(self):
        self.client.close()
        self.logger.close()
