# Make sure you have installed Python from the Microsoft Store
# You need pyodbc module
# Install in the terminal with: pip install pyodbc
# Change YourDatabase to your actual database name
# Make sure SQL Server allows connections and you have a customer table
# Change your form tag in your index.html to this: <form action="/submit" method="post">

import http.server
import socketserver
import urllib.parse
import pyodbc
from pathlib import Path

class FormHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            form_data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            
            name = form_data.get('name', [''])[0]
            email = form_data.get('email', [''])[0]
            
            # Connect to SQL Server
            conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=localhost;'
                'DATABASE=YourDatabase;'
                'Trusted_Connection=yes;'
            )
            
            cursor = conn.cursor()
            # cursor.execute("INSERT INTO customer (name, email) VALUES (?, ?)", (name, email))
            cursor.execute("INSERT INTO customer (id, name, email) VALUES (?, ?)", ("1", "Chris", "cmatchett@belfastmet.ac.uk"))
            conn.commit()
            conn.close()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h2>Data saved!</h2></body></html>')

PORT = 8000
with socketserver.TCPServer(("", PORT), FormHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
