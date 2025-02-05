from okex.core.core import OkexApi

class ProApi(OkexApi):
    def available_coin(self):
        """
        https://docs.ok-ex.io/?python#available-coin
        """
        return self._request('GET', '/oapi/v1/market/tickers')

    def coin_details(self, symbol):
        """
        https://docs.ok-ex.io/?python#coin-details
        :symbol Require
        """
        params = {
            'symbol': symbol
        }
        return self._request('GET', '/oapi/v1/market/ticker', params=params)

    def orderbooks(self, symbol):
        """
        https://docs.ok-ex.io/?python#orderbooks
        :symbol Require
        """
        params = {
            'symbol': symbol
        }
        return self._request('GET', '/oapi/v1/market/orderbook', params=params)

    def trade_history(self, symbol):
        """
        https://docs.ok-ex.io/?python#trade-history
        :symbol Require
        """
        params = {
            'symbol': symbol
        }
        return self._request('GET', '/oapi/v1/market/trades', params=params)

    def user_open_orders(self):
        """
        https://docs.ok-ex.io/?python#user_open_orders
        """
        return self._request('GET', '/oapi/v1/trade/market/orderbook')

    def user_trade_history(self):
        """
        https://docs.ok-ex.io/?python#user-trade-history
        """
        return self._request('GET', '/oapi/v1/trade/market/history')

    def trade_order(self):
        """
        https://docs.ok-ex.io/?python#trade-order
        """
        return self._request('GET', '/oapi/v1/trade/market/history')



