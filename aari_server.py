import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import threading

import aari


DEFAULT_PORT = 4789
ALLOWED_SIGNATURE = str(aari.load_config().get("signature", ""))


class AariRequestHandler(http.server.BaseHTTPRequestHandler):
    """Simple HTTP request handler for Aari commands."""

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/ping":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"pong")
            return

        if parsed.path == "/say":
            params = parse_qs(parsed.query)
            text = params.get("text", [""])[0]
            signature = params.get("signature", [""])[0]
            if signature != ALLOWED_SIGNATURE:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Forbidden")
                return
            lang = aari.load_config().get("language")
            try:
                aari.say(text, lang)
            except Exception:
                # ignore voice output errors for server usage
                pass
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
            return

        self.send_response(404)
        self.end_headers()


def run_server(host="0.0.0.0", port=DEFAULT_PORT):
    """Start the HTTP server."""
    with socketserver.TCPServer((host, port), AariRequestHandler) as httpd:
        print(f"[Aari] Server running on {host}:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:  # pragma: no cover - manual stop
            pass


if __name__ == "__main__":  # pragma: no cover - manual start
    run_server()
