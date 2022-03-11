
from Connection import TextWebsocketClient


#stream2 = TextWebsocketClient(products=['-USD'], channels = ['ticker'])
stream = TextWebsocketClient(products=['DOGE-USD'], channels = ['ticker'])
stream.start()
#stream.close()
