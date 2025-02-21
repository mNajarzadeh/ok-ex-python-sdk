from okex.core.core import OkexApi, OrderType, Side, Mode

class ProApi(OkexApi):
    def available_coin(self):
        """
        https://docs.ok-ex.io/?python#available-coin
        """
        return self._request('GET', '/oapi/v1/market/tickers')

    def coin_details(self, symbol:str):
        """
        https://docs.ok-ex.io/?python#coin-details
        :symbol Require
        """
        params = {
            'symbol': symbol
        }
        return self._request('GET', '/oapi/v1/market/ticker', params=params)

    def orderbooks(self, symbol:str):
        """
        https://docs.ok-ex.io/?python#orderbooks
        :symbol Require
        """
        params = {
            'symbol': symbol
        }
        return self._request('GET', '/oapi/v1/market/orderbook', params=params)

    def trade_history(self, symbol:str):
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

    def trade_order(self, quantity:str, symbol:str, o_type: OrderType, side:Side, price:str = None, stop_price:str = None):
        """
        https://docs.ok-ex.io/?python#trade-order
        :quantity Require
        :symbol Require
        :o_type Require order type define as enum
        :side Require
        :price require except market o_type
        :stop_price require on stop loss o_type
        """
        params = {
            'quantity': quantity,
            'symbol': symbol,
            'type': o_type.name,  #(LIMIT , MARKET , STOP_LOSS)
            'side': side
        }
        if o_type != OrderType.MARKET:
            params['price'] = price
        if o_type == OrderType.STOP_LOSS:
            params['stop_price'] = stop_price
        return self._request('POST', '/oapi/v1/trade/market', params=params)

    def order_cancel(self, order_id:str):
        """
        https://docs.ok-ex.io/?python#order-cancel
        :order_id Require
        """
        params = {
            'order_id': order_id
        }
        return self._request('POST', '/oapi/v1/trade/market/cancel', params=params)

    def order_receipt(self, order_id:str):
        """
        https://docs.ok-ex.io/?python#order-receipt
        :order_id Require
        """
        params = {
            'order_id': order_id
        }
        return self._request('POST', '/oapi/v1/trade/market/fills', params=params)