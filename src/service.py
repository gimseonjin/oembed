import requests

from src.oEmbed_client import oEmbed_client


client = oEmbed_client()


def get_oEmbed_from_url(url: str) :
    return client.get_oEmbed_data(url)
