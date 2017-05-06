#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Cvm(Base):
    requestHost = 'cvm.api.qcloud.com'

def main():
    action = 'DescribeInstances'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Cvm(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()