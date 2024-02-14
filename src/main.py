from src.iptc_fiddler import IPTCFiddler

if __file__ == "__main__":
    iptcf = IPTCFiddler()
    print(iptcf.read_headers('images/photo-4iptc-heads.jpg'))
