from colorama import Fore, Style

from web3pi_tunnel.config.srvconf import UPNP_DISCOVERY_TIMEOUT, UPNP_LEASE_TIME, USE_UPNP, PUBLIC_SERVICE
from web3pi_tunnel.tunnel_server.upnp.ipgetter import my_public_ip
from web3pi_tunnel.tunnel_server.upnp.upnpportmapper import BasicUPnPPortMapper


class BasicUPnPService:

    def __init__(self, tunnel_listen_port: int, proxy_establish_port: int, public_listen_port: int) -> None:
        self.upnp = None
        self.tunnel_listen_port = tunnel_listen_port
        self.proxy_establish_port = proxy_establish_port
        self.public_listen_port = public_listen_port

    def try_init_upnp(self, timeout: float = UPNP_DISCOVERY_TIMEOUT) -> bool:
        assert self.upnp is None

        ip = None
        res = False

        if USE_UPNP:
            print("Initializing UPnP service")
            self.upnp = BasicUPnPPortMapper()
            upnp_initialized = self.upnp.initialize(timeout)

            if not upnp_initialized:
                print("UPnP service: Failed to detect a device !!")
            else:
                print("UPnP service: Trying to map ports via UPnP")

                ports = [self.tunnel_listen_port, self.proxy_establish_port, self.public_listen_port]
                rules = ["Tunnel Conf Port", "Proxy Conf Port", "Public Listen Port"]
                res = self.upnp.add_multiple_mappings(ports, rules, UPNP_LEASE_TIME)

                if not res:
                    print("UPnP service: port forwarding -> FAILURE")
                else:
                    print(f"UPnP service: All ports forwarded successfully")
                    print(f"    Tunnel configuration port:  {self.tunnel_listen_port}")
                    print(f"    Proxy configuration port:   {self.proxy_establish_port}")
                    print(f"    Public service listen port: {self.public_listen_port}")

                    ip = self.upnp.get_external_ip_address()

        if ip is None:
            if PUBLIC_SERVICE:
                ip = my_public_ip()
            else:
                ip = "127.0.0.1"

        print(f"Service bound to ip address: " + Fore.LIGHTGREEN_EX + f"{ip}" + Style.RESET_ALL)

        return res

    def close_upnp(self):
        if USE_UPNP:
            print("UPnP service: shutting down - closing all mapped ports")

            if self.upnp.is_upnp_available():
                self.upnp.delete_all_created_mappings()

            print("UPnP service: shutdown complete")
