import json
from abc import ABC


#    {
#         "type": "image",
#         "image": {
#           "link": "http(s)://the-url",
#           # provider is an optional parameter
#           "provider": {
#             "name" : "provider-name"
#           },
#         }
#     }


class Image(ABC):
    def __init__(self, link: str, provider: str | None = None) -> None:
        self.link = link
        self.provider = provider

    def __str__(self):
        image = {
            "type": "image",
            "image": {
                "link": self.link,
                "provider": {"name": self.provider} if self.provider else None
            }
        }
        return json.dumps(image)


    def __repr__(self):
        return f"ImageComponent(link={self.link}, provider={self.provider})"


    def __eq__(self, other):
        return self.link == other.link and self.provider == other.provider