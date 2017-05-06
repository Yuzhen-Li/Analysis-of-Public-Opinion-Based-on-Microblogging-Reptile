#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Vpc(Base):
    requestHost = 'vpc.api.qcloud.com'

def main():
    action = 'DescribeVpcs'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Vpc(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
