#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Image(Base):
    requestHost = 'image.api.qcloud.com'

def main():
    action = 'DescribeCdbInstances'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Image(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()