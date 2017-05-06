#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Live(Base):
    requestHost = 'live.api.qcloud.com'

def main():
    action = 'DescribeLVBOnlineUsers'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Live(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
