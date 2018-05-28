from requests_oauthlib import OAuth1Session
from api.json_connector import JSONConnector
from api.api_config import APIConfig
import webbrowser
import time


class OAuthProcess:
    REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
    ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
    AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
    SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'

    @staticmethod
    def start_oauth(consumer_key, consumer_secret):
        oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri='oob')

        try:
            resp = oauth_client.fetch_request_token(OAuthProcess.REQUEST_TOKEN_URL)
        except ValueError as e:
            raise 'Invalid response from Twitter requesting templates token: {0}'.format(e)

        url = oauth_client.authorization_url(OAuthProcess.AUTHORIZATION_URL)

        webbrowser.open(url)

        json_data = {
            'consumer_key': consumer_key,
            'consumer_secret': consumer_secret,
            'oauth_token': resp.get('oauth_token'),
            'oauth_token_secret': resp.get('oauth_token_secret'),
            'timestamp': int(time.time())
        }

        JSONConnector.set_json_file_content(
            directory=APIConfig.json_save_path,
            name=APIConfig.json_oauth_file_name,
            data=json_data
        )

        return json_data

    @staticmethod
    async def confirm_with_pin(consumer_key, consumer_secret, oauth_token, oauth_token_secret, pin_code):
        oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
                                     resource_owner_key=oauth_token,
                                     resource_owner_secret=oauth_token_secret,
                                     verifier=pin_code)

        try:
            resp = oauth_client.fetch_access_token(OAuthProcess.ACCESS_TOKEN_URL)
        except ValueError as e:
            raise 'Invalid response from Twitter requesting templates token: {0}'.format(e)

        at = resp.get('oauth_token')
        ats = resp.get('oauth_token_secret')

        return {
            'access_token': at,
            'access_token_secret': ats
        }
