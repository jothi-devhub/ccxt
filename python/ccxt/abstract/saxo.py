from ccxt.base.types import Entry


class ImplicitAPI:
        
    #Entry def __init__(self, path, api, method, config):
    Account_Values = AccountValues = Entry('openapi/hist/v3/accountValues/{ClientKey}/', 'openapi', 'GET', {'cost':1})
    Info_price_Specific_instrument = InfopriceSpecificinstrument = Entry('openapi/trade/v1/infoprices', 'openapi', 'GET', {'cost':1)
    Info_price_list_instrument = Infopricelistinstrument = Entry('openapi/trade/v1/infoprices/list', 'openapi', 'GET', {'cost':1})                                                                                   
    Info_Price_Subscription = InfoPriceSubscription = Entry('openapi/trade/v1/infoprices/subscriptions', 'openapi', 'POST', {'cost':1})
    Remove_Info_Price_Subscriptions_By_Tag = RemoveInfoPriceSubscriptionsByTag = Entry ('openapi/trade/v1/infoprices/subscriptions/{ContextId}', 'openapi', 'DELETE', {'cost':202})
    Remove_Info_Price_Subscription_By_Id = RemoveInfoPriceSubscriptionById = Entry ('openapi/trade/v1/infoprices/subscriptions/{ContextId}/{ReferenceId}', 'openapi', 'DELETE', {'cost':202}                                                                                                                   
    Place_New_Order = PlaceNewOrder = Entry('openapi/trade/v2/orders', 'openapi' , 'POST' ,{'cost':1})
    Change_Order = ChangeOrder = Entry('openapi/trade/v2/orders', 'openapi' , 'PATCH' ,{'cost':1})
    Cancel_Order = CancelOrder = Entry('openapi/trade/v2/orders', 'openapi' , 'DELETE' ,{'cost':1})
    Get_Chart_Data = GetChartData = Entry('openapi/chart/v1/charts', 'openai', 'GET', {'cost':1})
    Chart_Data_Subscription = ChartDataSubscription = Entry('openapi/chart/v1/charts/subscriptions', 'openai', 'POST', {'cost':1})
    Chart_Data_Remove_Subscriptions = ChartDataRemoveSubscriptions = Entry('openapi/chart/v1/charts/subscriptions/{ContextId}', 'openai', 'DELETE', {'cost':1})
                                                                                    
    
