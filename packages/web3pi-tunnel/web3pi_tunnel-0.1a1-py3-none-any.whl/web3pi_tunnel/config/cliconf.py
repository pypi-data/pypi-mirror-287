import os
from dotenv import dotenv_values

env = {
    **dotenv_values(".env"),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

# TUNNEL SERVICE MANAGER LOCATION
# Provide a valid address of the tunnel service (e.g., a public IP)
TUNNEL_SERVICE_HOST = env.get("TUNNEL_SERVICE_HOST", "localhost")

# CLIENT HOST and PORT
CLIENT_SERVICE_HOST = env.get("CLIENT_SERVICE_HOST", "localhost")
CLIENT_SERVICE_PORT = int(env.get("CLIENT_SERVICE_PORT", "8545"))

# TUNNEL
RETRY_TIMEOUT = 10.0
