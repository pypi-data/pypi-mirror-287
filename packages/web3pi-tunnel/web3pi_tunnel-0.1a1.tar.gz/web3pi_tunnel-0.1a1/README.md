# Basic TCP Tunnel
PoC Python implementation of a basic TCP tunnel. Primary purpose: provide a public IP to clients behind NATs.

It was initially developed on **Windows 10 Pro** with **PyCharm 2022.3.1 (Community Edition)** and **Python 3.11** alongside the [Web3 Reverse Proxy](https://github.com/jimmyisthis/web3-reverse-proxy).


## Configure and Run
To configure and run this project, follow this [README.md](https://github.com/jimmyisthis/web3-reverse-proxy/blob/main/README.md).

### Client
- Add a valid server address to the `config/cliconf.py` file
- Make sure that the server is running
- Activate venv
- Run `basic_tcp_tunnel/client.py`

### Server
- Add a valid local address to the `config/srvconf.py` file (preferably a **public ip**)
- Activate venv
- Run `basic_tcp_tunnel/server.py`

## TODO
- Warnings
  - Response parser may fail (only rudimentary parsing was implemented)
