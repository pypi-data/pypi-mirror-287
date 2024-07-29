import socket


class TCPConnection:

    HOSTS = {}

    @classmethod
    def connect_raw(cls, host, port):
        if host not in cls.HOSTS:
            _host = socket.gethostbyname(host)
            cls.HOSTS[host] = _host

        host = cls.HOSTS[host]
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        return sock

    @classmethod
    def create_listen_socket(cls, listen_port: int):
        s_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_srv.bind(('0.0.0.0', listen_port))
        s_srv.listen(1)

        return s_srv
