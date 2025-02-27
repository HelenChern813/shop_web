from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Обработка входящих запросов"""

    def for_get(self):
        """Метод для обработки входящих GET-запросов"""

        path = self.path

        if path == "/css/bootstrap.min.css":
            path = "../css/bootstrap.min.css"
            type_header = "text/css"
        elif path == "/js/bootstrap.bundle.min.js":
            path = "../js/bootstrap.bundle.min.js"
            type_header = "text/javascript"

        else:
            path = "../html/contacts.html"
            type_header = "text/html"

        self.send_response(200)
        self.send_header("Content-type", type_header)
        self.end_headers()
        with open(path) as file:
            content = file.read()
            self.wfile.write(bytes(content, "utf-8"))

    def for_post(self):
        '''Метод для обработки POST-запросов'''
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        response = f"Received POST data: {post_data.decode('utf-8')}"
        print(response)


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
