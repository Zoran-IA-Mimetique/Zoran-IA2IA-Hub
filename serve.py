import http.server, socketserver, sys, os, pathlib
PORT=int(sys.argv[1]) if len(sys.argv)>1 else 8008
ROOT=pathlib.Path(__file__).resolve().parents[1]
os.chdir(ROOT)
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('',PORT),Handler) as httpd:
 print(f'Serving {ROOT} at http://127.0.0.1:{PORT}')
 httpd.serve_forever()
