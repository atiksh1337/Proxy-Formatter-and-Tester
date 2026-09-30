from urllib.parse import urlsplit, unquote
from validator import validate_proxy_fields


def parse_url_proxy(proxy):
    if "@" not in proxy:
        return None
    try:
        if "://" not in proxy:
            proxy = "//" + proxy
        parsed = urlsplit(proxy)
        username = unquote(parsed.username or "")
        password = unquote(parsed.password or "")
        host = parsed.hostname or ""
        port = parsed.port
        if port is None:
            return None
        port = str(port)
        if validate_proxy_fields(host, port, username, password):
            return username, password, host, port
    except ValueError:
        pass
    return None


def parse_colon_proxy(proxy):
    parts = proxy.split(":")
    if len(parts) != 4:
        return None
    host, port, username, password = parts
    if validate_proxy_fields(host, port, username, password):
        return username, password, host, port
    return None


def parse_labeled_lines(lines):
    labels = {
        "ip": "host", "host": "host", "hostname": "host",
        "port": "port", "username": "username", "user": "username",
        "password": "password", "pass": "password"
    }
    fields = {}
    for line in lines:
        if ":" not in line:
            return None
        label, value = line.split(":", 1)
        key = labels.get(label.strip().lower())
        if not key or key in fields:
            return None
        fields[key] = value.strip()
    if all(k in fields for k in ("host", "port", "username", "password")):
        if validate_proxy_fields(fields["host"], fields["port"], fields["username"], fields["password"]):
            return fields["username"], fields["password"], fields["host"], fields["port"]
    return None


def parse_four_lines(lines):
    if len(lines) != 4:
        return None
    host, port, username, password = lines
    if ":" not in host and "@" not in host and validate_proxy_fields(host, port, username, password):
        return username, password, host, port
    return None


def normalize_proxy(proxy):
    proxy = proxy.strip()
    if not proxy:
        return None
    result = parse_url_proxy(proxy) or parse_colon_proxy(proxy)
    if result:
        u, p, h, port = result
        return f"{u}:{p}@{h}:{port}"
    return None
