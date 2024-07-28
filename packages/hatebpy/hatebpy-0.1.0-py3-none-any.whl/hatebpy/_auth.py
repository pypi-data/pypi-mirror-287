from abc import ABC, abstractmethod

from requests_oauthlib import OAuth1


class HatenaBookmarkAuth(ABC):
    @abstractmethod
    def get_auth_headers(self):
        pass


class OAuth1Auth(HatenaBookmarkAuth):

    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_token_secret):
        self.auth = OAuth1(
            consumer_key, consumer_secret, oauth_token, oauth_token_secret
        )

    def get_auth_headers(self):
        return self.auth
