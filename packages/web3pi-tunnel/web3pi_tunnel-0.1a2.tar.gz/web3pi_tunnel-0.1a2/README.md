# WEb3Pi Tunnel
PoC Python implementation of a basic TCP tunnel. Primary purpose: provide a public IP to clients behind NATs.

It was initially developed alongside the [Web3Pi Proxy](https://github.com/Web3-Pi/web3-reverse-proxy).

## Setup

Simply install `web3pi-tunnel` package using your Python package manager, using **pip** for example:

```bash
pip install web3pi-tunnel
```

## Configuration

Provide `.env` file or set the system environments with the following entries.

### Client

- `TUNNEL_SERVICE_HOST` - the network address of the tunnel server
- `CLIENT_SERVICE_HOST` - the network address of the client target service
- `CLIENT_SERVICE_PORT` - the port of the client target service
- `TUNNEL_ESTABLISH_PORT` - the port of the tunnel server
- `TUNNEL_SERVICE_AUTH_KEY` - the api key to authenticate at the tunnel server

### Server

- `SERVICE_PUBLIC_IP` - the network address of the tunnel server
- `SERVICE_PUBLIC_LISTEN_PORT` - the port of tunnel server for external web3 users
- `TUNNEL_ESTABLISH_PORT` - the port of the tunnel server for the tunnel client
- `PROXY_ESTABLISH_PORT` - the port of the tunnel server for stats
- `TUNNEL_SERVICE_AUTH_KEY` - the api key to authenticate the tunnel client
