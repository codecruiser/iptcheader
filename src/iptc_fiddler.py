import re

from bs4 import BeautifulSoup


class IPTCFiddler:

    xmpmeta = None
    data_json = None

    def traverse_data(self, data_level):
        # NOTE: be aware that recursive has its depth
        data_json = []
        for data in data_level.find_all(recursive=False):
            child_data = self.traverse_data(data)
            node_data = {
                "prefix": data.prefix,
                "name": data.name,
                "namespace": data.namespace,
            }
            if child_data:
                node_data["_data_"] = child_data
            else:
                node_data["text"] = data.text
            data_json.append(node_data)
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
