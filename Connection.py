import pandas as pd
import cbpro
public_client = cbpro.PublicClient()
from Connection_Credentials import (api_key, api_pass, api_secret)



class TextWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        #self.url = 'wss://ws-feed-public.sandbox.pro.coinbase.com'
        self.message_count = 0
        
    def on_message(self, msg):
        self.message_count += 1
        msg_type = msg.get('type', None)
        if msg_type == 'ticker':
            #time_val = msg.get('time', ('-'*27)) #{time_val:30}
            price_val = msg.get('price', None)
            price_val = float(price_val) if price_val is not None else 'None'
            product_id = msg.get('product_id', None)
            # to add a type /* channel type:{msg_type}
            print(f"{price_val:.3f}{product_id}\t")
            
    def on_close(self):
        print(f"<---Websocket connection closed--->\n\tTotal messages: {self.message_count}")



