import time
import select

from colorama import Fore, Style

from web3pi_tunnel.common.connection.tcpconnection import TCPConnection
from web3pi_tunnel.common.connection.tcpforwarder import TCPForwarder
from web3pi_tunnel.common.stats.tunnelstats import TCPTunnelStats

from web3pi_tunnel.config.srvconf import TUNNEL_KEEPALIVE_DELAY, TUNNEL_INTERRUPT_POLL_DELAY


class TCPTunnelSrv:

    def __init__(self, tunnel_client_socket, proxy_establish_port, ext_ip, ext_port):
        self.ext_ip = ext_ip
        self.ext_port = ext_port
        self.tunnel_cli_sock = tunnel_client_socket
        self.proxy_establish_port = proxy_establish_port
        self.ext_server_socket = None
        self.tunnel_server_socket = None
        self.last_poll_time = time.time()

    def accept_new_request(self):
        while True:
            ready_read, _, _ = select.select([self.ext_server_socket], [], [], TUNNEL_INTERRUPT_POLL_DELAY)

            if len(ready_read) > 0:
                # request_sock, request_addr = self.ext_server_socket.accept()
                # print(f"TCP TUNNEL: New remote request from {request_addr}")
                request_sock, _ = self.ext_server_socket.accept()
                return request_sock
            else:
                now = time.time()
                if now - self.last_poll_time > TUNNEL_KEEPALIVE_DELAY:
                    self.tunnel_cli_sock.sendall(b'KEEPALIVE')
                    self.last_poll_time = now

    def init_new_proxy_connection(self):
        self.tunnel_cli_sock.sendall(b"NEWCONN")
        cli_proxy_sock, cli_proxy_addr = self.tunnel_server_socket.accept()

        return cli_proxy_sock

    def run_forever(self, stats: TCPTunnelStats):

        print(f"TCP TUNNEL: New tunnel established. Sharing external address: "
              "" + Fore.LIGHTGREEN_EX + f"{self.ext_ip}:{self.ext_port}" + Style.RESET_ALL)

        forwarder = TCPForwarder(stats)

        self.ext_server_socket = TCPConnection.create_listen_socket(self.ext_port)
        self.tunnel_server_socket = TCPConnection.create_listen_socket(self.proxy_establish_port)

        while True:
            try:
                request_sock = self.accept_new_request()
                proxy_sock = self.init_new_proxy_connection()

                forwarder.spawn_forward_thread(request_sock, proxy_sock)

            except IOError:
                print("TCP TUNNEL: IO error - closing tunel")
                self.tunnel_cli_sock.close()
                raise
            except KeyboardInterrupt:
                raise
