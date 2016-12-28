from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

path = 'site.html'
text = open(path).read().lower()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>Hello!</body></html>"
            self.wfile.write(message)
            print message
            return

        if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body> &#161 Hola ! <a href = '/hello' > Back to Hello! </a> </body></html>"
            self.wfile.write(message)
            print message
            return

        if self.path.endswith("/"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += text
            self.wfile.write(message)
            print message
            return

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()