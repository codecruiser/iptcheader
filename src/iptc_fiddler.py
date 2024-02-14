import re

from bs4 import BeautifulSoup


class IPTCFiddler:

    xmpmeta = None
    data_json = None

    def traverse_data(self, data_level):
        # NOTE: be aware that recursive has its depth
        data_json = []
        for data in data_level.find_all(recursive=False):
            data_json.append({
                "prefix": data.prefix,
                "name": data.name,
                "namespace": data.namespace,
                "text": data.text,
                "_data_": self.traverse_data(data)
            })
        return data_json

    def extract_headers(self):
        if self.xmpmeta:
            soup = BeautifulSoup(self.xmpmeta, "xml")
            self.data_json = self.traverse_data(soup)

        return self.data_json

    def read_headers(self, path):
        with open(path, 'rb') as fh:
            content = fh.read()
            found_pattern = re.search(rb'<x:xmpmeta[^>]*>(.+)</x:xmpmeta[^>]*>', content, re.DOTALL)

            # print(re.search(rb'<x:xmpmeta([^>]*)>',  content, re.DOTALL))
            if found_pattern and found_pattern.groups():
                self.xmpmeta = found_pattern.groups()[0]

        return self.extract_headers()
