from okex.core.core import OkexApi, Side, Mode

class OtcApi(OkexApi):
    def available_otc_coin(self):
        """
        https://docs.ok-ex.io/?python#available-otc-coin
        """
        return self._request('GET', '/oapi/v1/otc/tickers')

    def otc_coin_details(self, asset:str):
        """
        https://docs.ok-ex.io/?python#otc-coin-details
        asset Require
        """
        return self._request('GET', '/oapi/v1/otc/ticker?asset='+ asset.upper())

    def otc_estimate(self, fromAsset:str, amount:int, side:Side, mode:Mode):
        """
        https://docs.ok-ex.io/?python#otc-estimate
        fromAsset Require
        amount Require
        side Require
        mode Require
        """
        params =  {
           "fromAsset": fromAsset,
           "amount": amount,
           "side": side.name,
           "mode": mode.name
        }
        return self._request('POST', '/api/v2/otc/estimate', params=params)

    def otc_estimate_public(self, fromAsset:str, amount:int, side:Side, mode:Mode):
        """
        https://docs.ok-ex.io/?python#otc-estimate-public
        fromAsset Require
        amount Require
        side Require
        mode Require
        """
        params =  {
           "fromAsset": fromAsset,
           "amount": amount,
           "side": side.name,
           "mode": mode.name
        }
        return self._request('POST', '/api/v2/otc/estimate/public', params=params)

    def trade_otc(self, cnvId:str):
        """
        https://docs.ok-ex.io/?python#trade-otc
        cnvId Require access from otc_estimate and otc_estimate_public
        """
        params =  {
           "cnvId": cnvId
        }
        return self._request('POST', '/api/v2/otc/convert', params=params)

    def trade_otc_history(self, side:Side):
        """
        https://docs.ok-ex.io/?python#trade-otc-history
        """
        return self._request('GET', '/oapi/v1/trade/otc/history?side='+ side.name)