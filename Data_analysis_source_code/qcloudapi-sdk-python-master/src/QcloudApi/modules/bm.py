#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Bm(Base):
    requestHost = 'bm.api.qcloud.com'

def main():
    action = 'DescribeDeviceClass'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Bm(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
