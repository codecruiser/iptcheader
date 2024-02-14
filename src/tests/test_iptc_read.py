import os

from src.iptc_fiddler import IPTCFiddler


def test_read_headers():
    iptc_fiddler = IPTCFiddler()
    print(os.path.abspath(__file__))
    filename = 'photo-4iptc-heads.jpg'
    headers = iptc_fiddler.read_headers(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'images', filename
    ))
    print(headers)
    assert 1==2
