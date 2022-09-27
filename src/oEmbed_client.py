import oembed
import requests
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


class oEmbed_client():

    def __init__(self):
        self.consumer = oembed.OEmbedConsumer()
        for response in requests.get("https://oembed.com/providers.json").json():
            endpoints = response["endpoints"]
            for endpoint in endpoints:
                if endpoint.get("schemes"):
                    get_endpoint = oembed.OEmbedEndpoint(endpoint["url"], \
                                                        endpoint["schemes"])
                    self.consumer.addEndpoint(get_endpoint)


    def get_oEmbed_data(self, url:str):
        return self.consumer.embed(url).getData()
