import logging
from tornado.web import Application, RequestHandler
from tornado.httputil import HTTPServerRequest
from typing import Callable


logging.getLogger("tornado.access").setLevel(logging.ERROR)
logging.getLogger("tornado.application").setLevel(logging.ERROR)
logging.getLogger("tornado.general").setLevel(logging.ERROR)


class Request(HTTPServerRequest):
    handler: RequestHandler


def server(get: Callable[[Request], str]=None, post: Callable[[Request], str]=None, port: int=8888, address: str=None, *_, **kwargs):
    get_, post_ = get, post
    
    class MiniHandler(RequestHandler):
        if get_:
            async def get(self):
                self.set_header("Access-Control-Allow-Origin", "*")
                self.request.handler = self
                self.write(get_(self.request))
        
        if post_:
            async def post(self):
                self.set_header("Access-Control-Allow-Origin", "*")
                self.request.handler = self
                self.write(post_(self.request))

    app = Application([(r"/.*", MiniHandler)])
    app.listen(port, address=address, **kwargs)
    print(f"cliapi server is running.")
    return app