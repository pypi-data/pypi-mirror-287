import os
import sys

if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import colorama

from web3pi_tunnel.tunnel_client.clienttunnelservice import ClientTunnelService
from web3pi_tunnel.tunnel_client.servicedescr import ServiceDescr

from web3pi_tunnel.config.conf import TUNNEL_ESTABLISH_PORT, PROXY_ESTABLISH_PORT, TUNNEL_SERVICE_AUTH_KEY
from web3pi_tunnel.config.cliconf import CLIENT_SERVICE_HOST, CLIENT_SERVICE_PORT, TUNNEL_SERVICE_HOST


def main():
    colorama.init()

    descr = ServiceDescr(CLIENT_SERVICE_HOST, CLIENT_SERVICE_PORT,
                         TUNNEL_SERVICE_HOST,
                         TUNNEL_ESTABLISH_PORT, PROXY_ESTABLISH_PORT,
                         TUNNEL_SERVICE_AUTH_KEY)

    service = ClientTunnelService(descr)
    service.run_forever()


if __name__ == "__main__":
    main()
