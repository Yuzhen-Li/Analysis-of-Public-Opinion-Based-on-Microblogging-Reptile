#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Monitor(Base):
    requestHost = 'monitor.api.qcloud.com'

def main():
    action = 'DescribeMetrics'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Monitor(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()