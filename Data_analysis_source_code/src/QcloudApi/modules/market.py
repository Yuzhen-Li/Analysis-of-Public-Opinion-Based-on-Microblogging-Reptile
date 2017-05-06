#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Market(Base):
    requestHost = 'market.api.qcloud.com'

def main():
    action = 'QueryVoucherData'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Market(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
