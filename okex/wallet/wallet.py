from okex.core.core import OkexApi

class WalletApi(OkexApi):
    def balance(self):
        """
        https://docs.ok-ex.io/?python#wallet
        """
        return self._request('GET', '/oapi/v1/wallet')

    def get_address(self, coin:str, network:str, update : bool = False):
        """
        https://docs.ok-ex.io/?python#get-address
        :coin Require
        :network Require
        :gen_addr Optional
        :update_addr Optional
        """
        params = {
            "coin": coin,
            "network": network,
            "gen_addr": 'true',
            "update_addr": 'false'
        }
        if update:
            params['gen_addr'] = 'false'
            params['update_addr'] = 'true'
        return self._request('POST', '/oapi/v1/wallet/deposit/address', params=params)

    def deposit_history(self):
        """
        https://docs.ok-ex.io/?python#deposit-history
        """
        return self._request('GET', '/oapi/v1/wallet/deposit/history')

    def withdrawal(self, coin:str, amount:str, to_address:str, network:str):
        """
        https://docs.ok-ex.io/?python#withdrawal
        :coin Require
        :amount Require
        :to_address Require
        :network Require
        """
        params = {
            "coin": coin,
            "amount": amount,
            "to_address": to_address,
            "network": network
        }
        return self._request('POST', '/oapi/v1/wallet/withdrawal', params=params)

    def withdrawal_history(self):
        """
        https://docs.ok-ex.io/?python#withdrawal-history
        """
        return self._request('GET', '/oapi/v1/wallet/withdrawal/history')

    def wallet_transfer(self, coin:str, amount:str, wallet_from:str, wallet_to:str):
        """
        https://docs.ok-ex.io/?python#wallet-transfer
        :coin Require
        :amount Require
        :to_address Require
        :network Require
        """
        params = {
            "coin": coin,
            "amount": amount,
            "wallet_from": wallet_from,
            "wallet_to": wallet_to
        }
        return self._request('POST', '/oapi/v1/wallet/transfer', params=params)

    def transfer_history(self):
        """
        https://docs.ok-ex.io/?python#transfer-history
        """
        return self._request('GET', '/oapi/v1/wallet/transfer/history')
