#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Eip(Base):
    requestHost = 'eip.api.qcloud.com'

def main():
    action = 'DescribeEip'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Eip(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
