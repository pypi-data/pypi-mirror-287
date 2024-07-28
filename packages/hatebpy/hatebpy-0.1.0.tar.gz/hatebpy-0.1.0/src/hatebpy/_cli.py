import logging
import pprint
import webbrowser
from urllib.parse import urljoin, parse_qsl

import fire
import requests
from requests_oauthlib import OAuth1

BASE_URL = "https://www.hatena.com/"

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class AuthError(Exception):
    pass


def _get_scope_settings(scope: int) -> str:
    scope_params = []
    if scope & 1:
        scope_params.append("read_public")
    if scope & 2:
        scope_params.append("write_public")
    if scope & 4:
        scope_params.append("read_private")
    if scope & 8:
        scope_params.append("write_private")
    scope_str = ",".join(scope_params)
    return scope_str


def _get_oauth_token(
    consumer_key: str, consumer_secret: str, callback_uri: str, scope: int
) -> dict:
    initiate_url = urljoin(BASE_URL, "oauth/initiate")
    auth = OAuth1(consumer_key, consumer_secret, callback_uri=callback_uri)
    params = {"scope": _get_scope_settings(scope)}
    response = requests.post(initiate_url, auth=auth, params=params)
    token = dict(parse_qsl(response.text))
    if "oauth_problem" in token:
        raise AuthError(f"Error: {token['oauth_problem']}")
    return token


def _get_user_authorization(oauth_token: str) -> str:
    authorize_url = urljoin(BASE_URL, "oauth/authorize")
    auth_url = f"{authorize_url}?oauth_token={oauth_token}&perms=delete"
    webbrowser.open(auth_url)
    return input("Please enter the PIN code displayed after authentication: ")


def _get_access_token(
    consumer_key: str, consumer_secret: str, token: dict, oauth_verifier: str
) -> dict:
    access_token_url = urljoin(BASE_URL, "oauth/token")
    auth = OAuth1(
        consumer_key,
        consumer_secret,
        token["oauth_token"],
        token["oauth_token_secret"],
        verifier=oauth_verifier,
    )
    response = requests.post(access_token_url, auth=auth)
    access_token = dict(parse_qsl(response.text))
    if "oauth_problem" in access_token:
        raise AuthError(f"Error: {access_token['oauth_problem']}")
    return access_token


def _auth_flow(
    consumer_key: str, consumer_secret: str, callback_uri: str = "oob", scope: int = 15
) -> None:
    token = _get_oauth_token(consumer_key, consumer_secret, callback_uri, scope)
    oauth_verifier = _get_user_authorization(token["oauth_token"])
    access_token = _get_access_token(
        consumer_key, consumer_secret, token, oauth_verifier
    )

    logger.info("The access token is as follows:")
    final_params = {
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret,
        **access_token,
    }
    # Generate formatted output using pprint and log it
    formatted_output = pprint.pformat(final_params, indent=2)
    logger.info("\n%s", formatted_output)


def main():
    fire.Fire(_auth_flow)


if __name__ == "__main__":
    main()
