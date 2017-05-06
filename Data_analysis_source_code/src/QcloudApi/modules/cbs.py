#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Cbs(Base):
    requestHost = 'cbs.api.qcloud.com'

def main():
    action = 'DescribeCbsStorages'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Cbs(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
