import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# In-memory database
books = []

class BookHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/books':
            self._set_headers()
            self.wfile.write(json.dumps(books).encode())
        elif parsed_path.path.startswith('/books/'):
            book_id = int(parsed_path.path.split('/')[-1])
            book = next((book for book in books if book['id'] == book_id), None)
            if book:
                self._set_headers()
                self.wfile.write(json.dumps(book).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Book not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def do_POST(self):
        if self.path == '/books':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            book_data = json.loads(post_data.decode())
            book_data['id'] = len(books) + 1
            books.append(book_data)
            self._set_headers(201)
            self.wfile.write(json.dumps(book_data).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def do_PUT(self):
        if self.path.startswith('/books/'):
            book_id = int(self.path.split('/')[-1])
            book = next((book for book in books if book['id'] == book_id), None)
            if book:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                updated_data = json.loads(post_data.decode())
                book.update(updated_data)
                self._set_headers()
                self.wfile.write(json.dumps(book).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Book not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def do_DELETE(self):
        if self.path.startswith('/books/'):
            book_id = int(self.path.split('/')[-1])
            book = next((book for book in books if book['id'] == book_id), None)
            if book:
                books.remove(book)
                self._set_headers()
                self.wfile.write(json.dumps({"message": "Book deleted"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Book not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

def run(server_class=HTTPServer, handler_class=BookHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()


