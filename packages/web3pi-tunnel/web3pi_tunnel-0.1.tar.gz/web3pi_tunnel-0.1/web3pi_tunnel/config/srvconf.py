import os
from dotenv import dotenv_values

env = {
    **dotenv_values(".env"),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

# SERVICE PUBLIC INTERFACE
# Provide a valid public IP used by this server
SERVICE_PUBLIC_IP = env.get("SERVICE_PUBLIC_IP", "localhost")
SERVICE_PUBLIC_LISTEN_PORT = int(env.get("SERVICE_PUBLIC_LISTEN_PORT", "6512"))

ACCEPT_TIMEOUT = 2.5

# TUNNEL
TUNNEL_KEEPALIVE_DELAY = 25.0
TUNNEL_INTERRUPT_POLL_DELAY = 4.0

# UPnP
PUBLIC_SERVICE = True
USE_UPNP = env.get("USE_UPNP", "False").lower() in ['true', '1', 't', 'y', 'yes']
UPNP_DISCOVERY_TIMEOUT = 0.5
UPNP_LEASE_TIME = 1 * 3600
