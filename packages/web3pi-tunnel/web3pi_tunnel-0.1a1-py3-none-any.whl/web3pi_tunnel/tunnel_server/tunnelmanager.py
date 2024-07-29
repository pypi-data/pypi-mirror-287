from colorama import Fore, Style

import select

from web3pi_tunnel.common.connection.tcpconnection import TCPConnection
from web3pi_tunnel.config.srvconf import SERVICE_PUBLIC_IP, SERVICE_PUBLIC_LISTEN_PORT, ACCEPT_TIMEOUT
from web3pi_tunnel.config.conf import TUNNEL_SERVICE_AUTH_KEY
from web3pi_tunnel.tunnel_server.tunnel.tcptunnelsrv import TCPTunnelSrv


class TunnelManager:

    def __init__(self, tunnel_conf_listen_port: int, proxy_establish_port: int):
        self.service_pub_ip = SERVICE_PUBLIC_IP
        self.service_pub_port = SERVICE_PUBLIC_LISTEN_PORT

        self.allowed_user_api_key = TUNNEL_SERVICE_AUTH_KEY

        self.tunnel_conf_listen_port = tunnel_conf_listen_port
        self.proxy_establish_port = proxy_establish_port

        self.service_socket = TCPConnection.create_listen_socket(tunnel_conf_listen_port)

        print(f"TUNNEL MANAGER: Started new tunnel service to forward data from "
              "" + Fore.LIGHTGREEN_EX + f"{self.service_pub_ip}:{self.service_pub_port}" + Style.RESET_ALL)
        print(f"TUNNEL MANAGER: Configuration options - tunnel config port {tunnel_conf_listen_port}, proxy config port"
              f" {proxy_establish_port}, allowed api key {self.allowed_user_api_key}")

    def is_allowed(self, cli_sock):
        user_api_key = cli_sock.recv(2048).decode("utf-8")

        print(f"TUNNEL MANAGER: Authorizing {user_api_key} user API key...")
        if user_api_key != self.allowed_user_api_key:
            print(f"TUNNEL MANAGER: User api key {user_api_key} not authorized - disconnecting")
            return False

        print(f"TUNNEL MANAGER: User API key {user_api_key} authorized")

        return True

    def register_new_user(self, user_api_key: str):
        self.allowed_user_api_key = user_api_key

    def accept_tunnel_init_connection(self, timeout: float = ACCEPT_TIMEOUT):
        while True:
            ready_read, _, _ = select.select([self.service_socket], [], [], timeout)

            if len(ready_read) > 0:
                cli_sock, cli_addr = self.service_socket.accept()
                print(f"TUNNEL MANAGER: New tunnel init request from {cli_addr}")

                return cli_sock

    def wait_for_tunnel_request(self) -> TCPTunnelSrv:
        print("TUNNEL MANAGER: Waiting for a new tunnel to be established")

        while True:
            tunnel_cli_sock = self.accept_tunnel_init_connection()

            if self.is_allowed(tunnel_cli_sock):
                tunnel_cli_sock.sendall(f'ACPT|{self.service_pub_ip}:{self.service_pub_port}'.encode("utf-8"))

                return TCPTunnelSrv(tunnel_cli_sock, self.proxy_establish_port, self.service_pub_ip, self.service_pub_port)
            else:
                tunnel_cli_sock.close()

    def restart(self):
        self.service_socket.close()
        self.service_socket = TCPConnection.create_listen_socket(self.tunnel_conf_listen_port)

    def shutdown(self):
        print("TUNNEL MANAGER: shutting down tunnel manager")
        self.service_socket.close()
