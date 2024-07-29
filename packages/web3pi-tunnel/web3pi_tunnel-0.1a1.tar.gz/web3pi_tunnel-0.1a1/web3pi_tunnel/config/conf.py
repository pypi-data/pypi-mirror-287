import os
from dotenv import dotenv_values

env = {
    **dotenv_values(".env"),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

# SERVICE PUBLIC INTERFACE
TUNNEL_ESTABLISH_PORT = int(env.get("TUNNEL_ESTABLISH_PORT", "7634"))
PROXY_ESTABLISH_PORT = int(env.get("PROXY_ESTABLISH_PORT", "7835"))

# STATS
MAX_SHOW_STATS_RATE = 10.0

TUNNEL_SERVICE_AUTH_KEY = env.get("TUNNEL_SERVICE_AUTH_KEY", "")
