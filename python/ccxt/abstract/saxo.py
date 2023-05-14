from ccxt.base.types import Entry


class ImplicitAPI:
    
    #Entry def __init__(self, path, api, method, config):
    
    Post_place_Order = PostPlaceOrder = Entry('trade/v2/orders', 'openapi' , 'POST' ,{'cost':1})