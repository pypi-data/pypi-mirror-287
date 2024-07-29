from dataclasses import dataclass


@dataclass
class ServiceDescr:
    loc_service_host: str
    loc_service_port: int

    tunnel_service_host: str
    tunnel_establish_port: int
    proxy_establish_port: int

    user_api_key: str
