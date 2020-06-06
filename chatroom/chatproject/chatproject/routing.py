
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chatapp import routing


application = ProtocolTypeRouter({
   
   'websocket' : AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns) ),

})



