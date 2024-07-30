# WEb3Pi Tunnel

PoC Python implementation of a basic TCP tunnel. Primary purpose: provide a public IP to clients behind NATs.

It was initially developed alongside the [Web3Pi Proxy](https://github.com/Web3-Pi/web3-reverse-proxy).
There are two parts of the tunnel: the server which accepts connections from external users and forwards
to the client, and the client which forwards connections further to a target service.

## Configure and Run

### Setup

Simply install `web3pi-tunnel` package using your Python package manager, using **pip** for example:

```bash
pip install web3pi-tunnel
```

### Configuration

Create the `.env` file or set the system environments with the following entries.

#### Server

- `SERVICE_PUBLIC_IP` - the network address of the tunnel server
- `SERVICE_PUBLIC_LISTEN_PORT` - the port of tunnel server for external web3 users
- `TUNNEL_ESTABLISH_PORT` - the port of the tunnel server for the tunnel client
- `PROXY_ESTABLISH_PORT` - the port of the tunnel server for stats
- `TUNNEL_SERVICE_AUTH_KEY` - the api key to authenticate the tunnel client, any random character string
- `USE_UPNP` - should the tunnel server use UPnP for the service, default value is `False`, may be set to `True`, optional

The example of the `.env` file

```text
SERVICE_PUBLIC_IP=127.0.0.1
SERVICE_PUBLIC_LISTEN_PORT=6512
TUNNEL_ESTABLISH_PORT=7634
PROXY_ESTABLISH_PORT=7835
TUNNEL_SERVICE_AUTH_KEY=aaa
```

#### Client

- `TUNNEL_SERVICE_HOST` - the network address of the tunnel server
- `CLIENT_SERVICE_HOST` - the network address of the client target service
- `CLIENT_SERVICE_PORT` - the port of the client target service
- `TUNNEL_ESTABLISH_PORT` - the port of the tunnel server
- `TUNNEL_SERVICE_AUTH_KEY` - the api key to authenticate the tunnel client, any random character string

The example of the `.env` file

```text
TUNNEL_SERVICE_HOST=127.0.0.1
CLIENT_SERVICE_HOST=127.0.0.1
CLIENT_SERVICE_PORT=8545
TUNNEL_ESTABLISH_PORT=7634
TUNNEL_SERVICE_AUTH_KEY=aaa
```

### Run

#### Server

Execute the command

```bash
web3pi_tunnel_server
```

#### Client

Execute the command

```bash
web3pi_tunnel_client
```
