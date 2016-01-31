import SimpleHTTPServer
import SocketServer

PORT = 8000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.warning("======= GET STARTED =======")
        logging.warning(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.warning("======= POST STARTED =======")
        logging.warning(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        logging.warning("======= POST VALUES =======")
        for item in form.list:
            logging.warning(item)
        logging.warning("\n")
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
print "Python http server version 0.1 (for testing purposes only)"
print "Serving at: http://%(interface)s:%(port)s" % dict(interface="localhost", port=PORT)
httpd.serve_forever()