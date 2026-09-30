def classify_error(exc):
    msg = str(exc).lower()
    if "timed out" in msg or "timeout" in msg:
        return "Request timed out"
    if "proxy" in msg:
        return "Proxy connection failed"
    if "ssl" in msg or "certificate" in msg:
        return "SSL verification failed"
    if "could not resolve" in msg or "connection" in msg or "connect" in msg:
        return "Connection failed"
    return str(exc)
