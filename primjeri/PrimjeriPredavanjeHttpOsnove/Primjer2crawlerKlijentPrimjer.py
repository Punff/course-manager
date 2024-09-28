import socket, time, re

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print (e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)       
    
    return s

def get_source(s, ip, page):

    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF
    get += CRLF

    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    print (response)
    return response

def get_all_images(response):
    list_img = []
    beg = 0
    while True:
        beg_str = response.find('src="', beg)   
        if beg_str == -1:
            return list_img  
        end_str = response.find('"', beg_str + 5)      
        img = response[beg_str + 5:end_str]
        if img not in list_img:
            list_img.append(img)
        beg = end_str + 1
        



ip = 'www.optimazadar.hr'
port = 80
page = '1280/djelatnost1280.html'
s = connect_to_server(ip, port)
print (s)
response = get_source(s, ip, page)
print (get_all_images(response))

