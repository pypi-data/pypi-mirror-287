import os
import sys

if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import colorama

from web3pi_tunnel.tunnel_server.servertunnelservice import ServerTunnelService


def main():
    colorama.init()

    service = ServerTunnelService()
    service.run_forever()


if __name__ == "__main__":
    main()
