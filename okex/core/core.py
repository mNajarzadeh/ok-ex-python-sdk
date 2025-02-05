import datetime
import hmac
import hashlib
import requests
import json
class OkexApi(object):
    def __init__(self, api_key='', secret_key=''):
        """
        https://docs.ok-ex.io/?python#start-working
        """

        self.url = 'https://azapi.ok-ex.io'
        self.api_key = api_key
        self.secret_key= secret_key

    def _request(self, method, uri, params=None):
        """
        https://docs.ok-ex.io/?python#start-working
        header must have
        :Content-Type: application/json
        :x-api-key: you must create in your account  ok-ex.io
        :x-signature: 
        :x-timestamp: 
        """
        signed_key, timestamp = self.create_signature(uri, method)
        url = self.url+uri
        headers = {'Content-Type': 'application/json',
                    'x-api-key': self.api_key,
                    'x-signature': signed_key,
                    'x-timestamp': str(timestamp)}
        response = requests.get(url, params=params, headers=headers)
        return response.text



    def create_signature(self, full_path, request_method, request_data=None):
        timestamp = int( datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)
        msg = f'{request_method.upper()}\n{full_path}\n{timestamp}'

        if request_data:
            base64encode = base64.b64encode(json.dumps(request_data).encode()).decode()
            msg += f'\n{base64encode}'

        signed_key = hmac.new(
            bytes(self.secret_key, "utf-8"),
            msg=bytes(msg, "utf-8"),
            digestmod=hashlib.sha256).hexdigest()

        return signed_key, timestamp

