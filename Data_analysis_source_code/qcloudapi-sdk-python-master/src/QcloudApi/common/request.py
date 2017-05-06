#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import requests
from sign import Sign

class Request:
    timeout = 10
    version = 'SDK_PYTHON_1.1'
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey

    def generateUrl(self, requestHost, requestUri, params, method = 'GET'):
        params['RequestClient'] = Request.version
        sign = Sign(self.secretId, self.secretKey)
        params['Signature'] = sign.make(requestHost, requestUri, params, method)
        params = urllib.urlencode(params)

        url = 'https://%s%s' % (requestHost, requestUri)
        if (method.upper() == 'GET'):
            url += '?' + params

        return url

    def send(self, requestHost, requestUri, params, files = {}, method = 'GET', debug = 0):
        params['RequestClient'] = Request.version
        sign = Sign(self.secretId, self.secretKey)
        params['Signature'] = sign.make(requestHost, requestUri, params, method)

        url = 'https://%s%s' % (requestHost, requestUri)

        if (method.upper() == 'GET'):
            req = requests.get(url, params=params, timeout=Request.timeout, verify=False)
            if (debug):
                print 'url:', req.url, '\n'
        else:
            req = requests.post(url, data=params, files=files, timeout=Request.timeout, verify=False)
            if (debug):
                print 'url:', req.url, '\n'

        if req.status_code != requests.codes.ok:
            req.raise_for_status()

        return req.text

def main():
    secretId = 123
    secretKey = 'test'
    params = {}
    request = Request(secretId, secretKey)
    print request.generateUrl('cvm.api.qcloud.com', '/v2/index.php', params)
    print request.send('cvm.api.qcloud.com', '/v2/index.php', params)

if (__name__ == '__main__'):
    main()
