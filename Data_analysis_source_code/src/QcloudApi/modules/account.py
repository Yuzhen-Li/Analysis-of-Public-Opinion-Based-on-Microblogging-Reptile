#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Account(Base):
    requestHost = 'account.api.qcloud.com'

def main():
    action = 'AddProject'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Account(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
