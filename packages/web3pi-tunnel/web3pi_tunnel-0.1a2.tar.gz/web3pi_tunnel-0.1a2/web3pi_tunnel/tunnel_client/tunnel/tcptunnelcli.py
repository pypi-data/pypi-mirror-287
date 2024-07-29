import sys

import select

from web3pi_tunnel.common.connection.tcpconnection import TCPConnection
from web3pi_tunnel.common.connection.tcpforwarder import TCPForwarder
from web3pi_tunnel.common.stats.tunnelstats import TCPTunnelStats


class TCPTunnelCli:

    def __init__(self, tunnel_sock, loc_service_host: str, loc_service_port: int,
                 remote_service_host: str, proxy_establish_port: int):

        self.tunnel_sock = tunnel_sock

        self.loc_service_host = loc_service_host
        self.loc_service_port = loc_service_port

        self.remote_service_host = remote_service_host
        self.proxy_establish_port = proxy_establish_port

        self.stats = TCPTunnelStats("Received")

    def wait_for_request(self):
        while True:
            ready_read, _, _ = select.select([self.tunnel_sock], [], [])
            assert len(ready_read) == 1

            data = self.tunnel_sock.recv(2048)

            if len(data) == 0:
                print()
                print("TCP TUNNEL: Remote endpoint abruptly closed tunnel - shutting down")
                sys.exit(0)

            if data == b'KEEPALIVE':
                # print("TCP TUNNEL: KEEPALIVE packet received")
                pass
            else:
                assert data == b"NEWCONN", data
                # print(f"Connecting to {self.remote_service_host}:{self.proxy_establish_port} after NEWCONN")

                return TCPConnection.connect_raw(self.remote_service_host, self.proxy_establish_port)

    def init_new_local_connection(self):
        try:
            return TCPConnection.connect_raw(self.loc_service_host, self.loc_service_port)
        except IOError:
            print("TCP TUNNEL: Failed to open connection to the local service")
            return None

    def run_forever(self):
        print("TCP TUNNEL: Tunnel active - waiting for incoming connections")

        forwarder = TCPForwarder(self.stats)

        try:
            while True:
                remote_connection = self.wait_for_request()
                local_connection = self.init_new_local_connection()

                if local_connection is None:
                    remote_connection.close()
                else:
                    forwarder.spawn_forward_thread(remote_connection, local_connection)
        except KeyboardInterrupt:
            print()
            print("TCP TUNNEL: Interrupted by user - shutting down")
            self.tunnel_sock.close()
        except IOError:
            print()
            print("TCP TUNNEL: Remote endpoint stopped responding - shutting down")
            self.tunnel_sock.close()
