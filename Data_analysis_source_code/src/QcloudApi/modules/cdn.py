#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import os
from base import Base

class Cdn(Base):
    requestHost = 'cdn.api.qcloud.com'

    def UploadCdnEntity(self, params):
        action = 'UploadCdnEntity'
        if (params.get('entityFile') == None):
            raise ValueError, 'entityFile can not be empty.'
        if (os.path.isfile(params['entityFile']) == False):
            raise ValueError, 'entityFile is not exist.'

        file = params.pop('entityFile')
        if ('entityFileMd5' not in params):
            params['entityFileMd5'] = hashlib.md5(open(file, 'rb').read()).hexdigest()

        files = {
            'entityFile': open(file, 'rb')
        }

        return self.call(action, params, files)

def main():
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'post'
    }
    params = {
        'entityFileName': '/test.txt',
        'entityFile': '/tmp/test.txt'
    }
    service = Cdn(config)
    print service.UploadCdnEntity(params)

if (__name__ == '__main__'):
    main()
