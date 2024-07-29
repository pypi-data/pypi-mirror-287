from web3pi_tunnel.config.conf import TUNNEL_ESTABLISH_PORT, PROXY_ESTABLISH_PORT
from web3pi_tunnel.config.srvconf import SERVICE_PUBLIC_LISTEN_PORT

from web3pi_tunnel.common.stats.tunnelstats import TCPTunnelStats

from web3pi_tunnel.tunnel_server.tunnelmanager import TunnelManager
from web3pi_tunnel.tunnel_server.upnp.upnpservice import BasicUPnPService


class ServerTunnelService:

    def __init__(self, tunnel_listen_port: int = TUNNEL_ESTABLISH_PORT,
                 proxy_establish_port: int = PROXY_ESTABLISH_PORT):

        print("MAIN SERVICE: starting -> creating tunnel manager")
        self.tunnel_manager = TunnelManager(tunnel_listen_port, proxy_establish_port)
        self.stats = TCPTunnelStats("Forwarded")

    def run_forever(self):
        upnp_service = BasicUPnPService(TUNNEL_ESTABLISH_PORT, PROXY_ESTABLISH_PORT, SERVICE_PUBLIC_LISTEN_PORT)
        upnp_service.try_init_upnp()

        while True:
            try:
                tunnel = self.tunnel_manager.wait_for_tunnel_request()
                tunnel.run_forever(self.stats)
            except IOError:
                print()
                print("MAIN SERVICE: Active tunnel was abruptly closed - restarting tunnel")
                self.tunnel_manager.restart()
            except KeyboardInterrupt:
                print()
                print("MAIN SERVICE: User Interrupt - shutting down")
                self.tunnel_manager.shutdown()

                upnp_service.close_upnp()

                return
