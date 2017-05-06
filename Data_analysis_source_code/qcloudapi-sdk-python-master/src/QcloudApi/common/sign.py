#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii
import hashlib
import hmac

class Sign:
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey

    def make(self, requestHost, requestUri, params, method = 'GET'):
        list = {}
        flag_sha256 = 0
        for param_key in params:
            if method == 'post' and str(params[param_key])[0:1] == "@":
                continue
            if param_key == 'SignatureMethod' and params[param_key] == 'HmacSHA256':
                flag_sha256 = 1
            list[param_key] = params[param_key]
        srcStr = method.upper() + requestHost + requestUri + '?' + "&".join(k.replace("_",".") + "=" + str(list[k]) for k in sorted(list.keys()))
        if flag_sha256 == 1:
            hashed = hmac.new(self.secretKey, srcStr, hashlib.sha256)
        else:
            hashed = hmac.new(self.secretKey, srcStr, hashlib.sha1)    
        return binascii.b2a_base64(hashed.digest())[:-1]

def main():
    secretId = 123
    secretKey = 'xxx'
    params = {}
    sign = Sign(secretId, secretKey)
    print sign.make('https://cvm.api.qcloud.com', '/v2/index.php', params)

if (__name__ == '__main__'):
    main()
