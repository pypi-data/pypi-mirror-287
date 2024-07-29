import select

from threading import Thread

from web3pi_tunnel.common.stats.tunnelstats import TCPTunnelStats


class TCPForwarder:

    def __init__(self, stats: TCPTunnelStats):
        self.stats = stats

    def forward_impl(self, s_src, s_dst):
        # no = self.stats.num_connections
        self.stats.register_new_connection()

        # print(f"FORWARDER THREAD IMPL: TH START {no}")
        data_to_process = True

        while data_to_process:
            s_read, _, _ = select.select([s_src, s_dst], [], [])

            for s in s_read:
                data = s.recv(8192)

                if not data:
                    # print("No more data")
                    data_to_process = False
                    break

                if s == s_src:
                    # print(f"LOCAL <-- {len(data)} <-- REMOTE")
                    # print(data)
                    s_dst.sendall(data)
                    self.stats.register_inbound_packet(data)
                elif s == s_dst:
                    # print(f"LOCAL --> {len(data)} --> REMOTE")
                    # print(data)
                    s_src.sendall(data)
                    self.stats.register_outbound_packet(data)

        s_src.close()
        s_dst.close()

        # print(f"FORWARDER THREAD IMPL: TH END {no}")

    def spawn_forward_thread(self, s_src, s_dst):
        th = Thread(target=self.forward_impl, args=[s_src, s_dst], daemon=True)
        th.start()

    def forward(self, s_src, s_dst):
        self.forward_impl(s_src, s_dst)
