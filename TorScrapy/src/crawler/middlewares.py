from toripchanger import TorIpChanger
import os
import requests
TOR_PASSWORD = os.environ['TOR_PASSWORD'] 
tor_ip_changer = TorIpChanger(tor_password=TOR_PASSWORD, tor_port=9051, local_http_proxy='tor-proxy:8118',tor_address="tor-proxy",reuse_threshold=0,new_ip_max_attempts=20)

class ProxyMiddleware(object):
    _requests_count = 0
    
    
    def process_request(self, request, spider):
        #A Tor IP will be reused only after 10 different IPs were used.
        self._requests_count += 1
        if self._requests_count > 10:
            spider.log('Renewing IP after %s requests' % (self._requests_count - 1))
            self._requests_count = 0 
            tor_ip_changer.get_new_ip()
            spider.log("Current ip: {}".format(requests.get('https://api.myip.com/', proxies={'https': 'tor-proxy:8118'}).json()))
        request.meta['proxy'] = 'http://tor-proxy:8118'
