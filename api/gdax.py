
'https://www.kraken.com/help/api'

import requests
import json

class GDAX(object):

    def __init__(self):
        self.url = 'https://api.gdax.com'
        self.version = '0'

    def __args_string(self, data):
        return '?' + '&'.join([key + '=' + data[key] for key in data])

    def __query_public(self, urlpath, data=None):
        url = self.url +  urlpath
        if data:
            url += self.__args_string(data)
        response = requests.get(url)
        json_response = json.loads(response.content)
        return json_response

    def get_products(self, data=None):
        return self.__query_public('/products', data)

    def get_product_order_book(self, product_id, data=None):
        return self.__query_public('/products/%s/book' % (product_id), data)

    def get_product_ticker(self, product_id, data=None):
        return self.__query_public('/products/%s/ticker' % (product_id), data)

    def get_trades(self, product_id, data=None):
        return self.__query_public('/products/%s/trades' % (product_id), data)

    def get_historic_rates(self, product_id, data=None):
        return self.__query_public('/products/%s/candles' % (product_id), data)

    def get_24_hr_stats(self, product_id, data=None):
        return self.__query_public('/products/%s/stats' % (product_id), data)
       
    def get_currencies(self):
        return self.__query_public('/currencies') 

    def get_server_time(self):
        return self.__query_public('/time')


if __name__ == '__main__':
    g = GDAX()
    r = g.get_server_time()
    print r
