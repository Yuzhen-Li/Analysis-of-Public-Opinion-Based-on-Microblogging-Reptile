#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Sec(Base):
    requestHost = 'csec.api.qcloud.com'

def main():
    action = 'CaptchaQuery'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {
        'userIp': '127.0.0.1',
        'businessId': 1,
        'captchaType': 1,
        'script': 0,
    }
    service = Sec(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()