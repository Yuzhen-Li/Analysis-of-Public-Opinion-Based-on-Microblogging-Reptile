#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Cmem(Base):
    requestHost = 'cmem.api.qcloud.com'

def main():
    action = 'DescribeCmem'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Cmem(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()