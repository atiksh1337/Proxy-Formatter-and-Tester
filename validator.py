def validate_port(port):
    return bool(port and port.isdigit() and 1 <= int(port) <= 65535)


def validate_proxy_fields(host, port, username, password):
    return bool(host and username and password and validate_port(port))
