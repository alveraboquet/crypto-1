
'https://bittrex.com/home/api'

import requests
import json

class Bittrex(object):

    def __init__(self):
        self.url = 'https://bittrex.com/api/'
        self.version = 'v1.1'

    def __args_string(self, data):
        return '?' + '&'.join([key + '=' + data[key] for key in data])

    def __query_public(self, urlpath, data=None):
        url = self.url + self.version + '/public' + urlpath
        if data:
            url += self.__args_string(data)
        response = requests.get(url)
        json_response = json.loads(response.content)
        print json_response
        return json_response['result']

    def get_markets(self):
        return self.__query_public('/getmarkets')

    def get_currencies(self):
        return self.__query_public('/getcurrencies')

    def get_ticker(self, data):
        return self.__query_public('/getticker', data)

    def get_market_summaries(self):
        return self.__query_public('/getmarketsummaries')

    def get_market_summary(self, data):
        return self.__query_public('/getmarketsummary', data)

    def get_order_book(self, data):
        return self.__query_public('/getorderbook', data)

    def get_market_history(self, data):
        return self.__query_public('/getmarkethistory', data)

    
if __name__ == '__main__':
    r = Bittrex()
    data = {'market':'BTC-LTC'}
    s = r.get_market_history(data)
    print s
