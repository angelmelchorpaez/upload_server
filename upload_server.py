# upload_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class UploadHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)

        # Obtener el nombre del archivo desde una cabecera personalizada
        filename = self.headers.get('X-Filename', 'recibido.bin')

        with open(filename, 'wb') as f:
            f.write(content)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Archivo recibido correctamente.\n')

server = HTTPServer(('0.0.0.0', 8080), UploadHandler)
print("[*] Servidor de subida escuchando en puerto 8080...")
server.serve_forever()
