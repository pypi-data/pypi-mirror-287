import locale
import time

from web3pi_tunnel.config.conf import MAX_SHOW_STATS_RATE

from web3pi_tunnel.common.helpers.formatters import bytes2human


class TCPTunnelStats:

    def __init__(self, prefix: str, print_updates: bool = True):
        self.prefix = prefix

        self.num_connections = 0
        self.inbound_bytes = 0
        self.outbound_bytes = 0

        self.print_updates = print_updates
        self.update_delay = 1.0 / MAX_SHOW_STATS_RATE
        self.last_update_time = time.time() - self.update_delay

        self.started_at = time.time()

    def handle_update(self):
        if self.print_updates:
            now = time.time()
            if now - self.last_update_time > self.update_delay:
                in_speed = bytes2human(self.inbound_bytes / (now - self.started_at))
                out_speed = bytes2human(self.outbound_bytes / (now - self.started_at))

                print(f"\rSTATS:      "
                      f"{self.prefix} {locale.format_string('%d', self.num_connections)} connections, "
                      f"Inbound {bytes2human(self.inbound_bytes)} [@ avg speed: {in_speed}/s], "
                      f"Outbound {bytes2human(self.outbound_bytes)} [@ avg speed: {out_speed}/s]"
                      f"          ", end="")
                self.last_update_time = now

    def register_inbound_packet(self, data):
        self.inbound_bytes += len(data)
        self.handle_update()

    def register_outbound_packet(self, data):
        self.outbound_bytes += len(data)
        self.handle_update()

    def register_new_connection(self):
        self.num_connections += 1
        self.handle_update()
