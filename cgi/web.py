import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
cgi = '.' # место, где находятся файлы html и подкаталог cgi-bin
port = 80 
os.chdir(cgi) # перейти в корневой каталог HTML
srvraddr = ("", port) # имя хоста и номер порта
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever() # запустить как бесконечный фоновый процесс 
