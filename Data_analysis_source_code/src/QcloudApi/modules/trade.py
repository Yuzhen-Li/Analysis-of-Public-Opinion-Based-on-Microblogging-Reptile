#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Trade(Base):
    requestHost = 'trade.api.qcloud.com'

def main():
    action = 'DescribeAccountBalance'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Trade(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()