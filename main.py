import http.server
import socketserver

PORT = 8080


class MyHandler(http.server.SimpleHTTPRequestHandler):
    """Класс, который отвечает за
    обработку входящих запросов от клиентов"""

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""

        if self.path == "/contacts":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("contacts.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))
        elif self.path.startswith("/css/"):
            try:
                file_path = self.path[1:]  # Убираем первый символ '/'
                with open(file_path, "rb") as file:
                    self.send_response(200)
                    self.send_header("Content-type", "text/css")
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Сервер запущен на порту", PORT)
        httpd.serve_forever()
