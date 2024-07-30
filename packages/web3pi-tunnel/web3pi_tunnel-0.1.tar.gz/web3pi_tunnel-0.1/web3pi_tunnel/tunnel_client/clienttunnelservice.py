import sys
import time

from colorama import Fore, Style

from web3pi_tunnel.tunnel_client.servicedescr import ServiceDescr
from web3pi_tunnel.common.connection.tcpconnection import TCPConnection
from web3pi_tunnel.tunnel_client.tunnel.tcptunnelcli import TCPTunnelCli
from web3pi_tunnel.config.cliconf import RETRY_TIMEOUT


class ClientTunnelService:

    def __init__(self, descr: ServiceDescr) -> None:
        local_service_str = Fore.LIGHTGREEN_EX + f"{descr.loc_service_host}:{descr.loc_service_port}" + Style.RESET_ALL
        print(f"SERVICE: Starting service\n"
              f"    LOC_SERVICE:        {local_service_str}\n"
              f"    REMOTE_TUNNEL_CONF: {descr.tunnel_service_host}:{descr.tunnel_establish_port}\n"
              f"    REMOTE_PROXY_CONF:  {descr.tunnel_service_host}:{descr.proxy_establish_port}\n"
              f"    USER_API_KEY:       {descr.user_api_key}")

        self.loc_service_host = descr.loc_service_host
        self.loc_service_port = descr.loc_service_port

        self.tunnel_service_host = descr.tunnel_service_host
        self.tunnel_establish_port = descr.tunnel_establish_port
        self.proxy_establish_port = descr.proxy_establish_port

        self.user_api_key = descr.user_api_key.encode("utf-8")

    def establish_tunel(self) -> TCPTunnelCli:
        while True:
            try:
                print(f"SERVICE: Trying to establish tunnel to the remote server "
                      f"{self.tunnel_service_host}:{self.tunnel_establish_port}")

                tunnel_sock = TCPConnection.connect_raw(self.tunnel_service_host, self.tunnel_establish_port)
                tunnel_sock.sendall(self.user_api_key)
                response = tunnel_sock.recv(2048).decode("utf-8")

                if response.startswith("ACPT"):
                    print(f"SERVICE: Establishing new tunnel - forwarding data from the remote endpoint "
                          "" + Fore.LIGHTGREEN_EX + f"{response[5:]}" + Style.RESET_ALL + ""
                          f" -> to -> "
                          "" + Fore.LIGHTGREEN_EX + f"{self.loc_service_host}:{self.loc_service_port}"
                          "" + Style.RESET_ALL + " local endpoint")

                    return TCPTunnelCli(tunnel_sock, self.loc_service_host, self.loc_service_port,
                                        self.tunnel_service_host, self.proxy_establish_port)
                else:
                    print("SERVICE: Failed to establish tunnel with the remote server - remote server rejected auth "
                          "credentials")
                    tunnel_sock.close()
                    time.sleep(RETRY_TIMEOUT)
            except IOError:
                print("SERVICE: Failed to establish tunnel with remote server due to connection error")
                sys.exit(0)

    def run_forever(self):
        self.establish_tunel().run_forever()
