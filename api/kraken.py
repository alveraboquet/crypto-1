
'https://www.kraken.com/help/api'

import requests
import json

class Kraken(object):

    def __init__(self):
        self.url = 'https://api.kraken.com/'
        self.version = '0'

    def __args_string(self, data):
        return '?' + '&'.join([key + '=' + data[key] for key in data])

    def __query_public(self, urlpath, data=None):
        url = self.url + self.version + '/public' +  urlpath
	if data:
            url += self.__args_string(data)
	response = requests.get(url)
        json_response = json.loads(response.content)
        return json_response['result']

    def get_server_time(self):
        return self.__query_public('/Time')

    def get_asset_info(self, data=None):
        return self.__query_public('/Assets', data)

    def get_tradable_pairs(self, data=None):
        return self.__query_public('/AssetPairs', data)

    def get_ticker_info(self, data):
        return self.__query_public('/Ticker', data)

    def get_ohlc(self, data):
        return self.__query_public('/OHLC', data)

    def get_order_book(self, data):
        return self.__query_public('/Depth', data)

    def get_current_fair_px(self, data):
        ob = self.get_order_book(data)[data['pair']]
        bids, ask = ob['bids'], ob['asks']
        best_bid, best_ask = float(bids[0][0]), float(bids[0][0])
        return (best_bid + best_ask) / 2.

    def get_recent_trades(self, data):
        return self.__query_public('/Trades', data)

    def get_recent_spreads(self, data):
        return self.__query_public('/Spread', data)

'''if __name__ == '__main__':
    k = Kraken()
    r = k.get_current_fair_px({'pair':'XXBTZUSD'})
    print r
'''
