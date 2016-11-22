def app(environ, start_response):
        query = environ["QUERY_STRING"]
        data_list = query.split("&")
        data = "\n".join(data_list)
        data = bytes(data)
#        data = bytes(data,'utf-8')
        start_response("200 OK",[("Content-Type","text/plain"),("Content-Length",str(len(data)))])
        return [data]
