#coding=utf8
   
import urllib
import urllib2
import cookielib
import base64
import re
import json
import hashlib
import rsa
import binascii

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
postdata = {
     'entry': 'weibo',
     'gateway': '1',
     'from': '',
     'savestate': '7',
     'userticket': '1',
     'ssosimplelogin': '1',
     'vsnf': '1',
      'vsnval': '',
      'su': '',
      'service': 'miniblog',
      'servertime': '',
      'nonce': '',
      'pwencode': 'rsa2', #加密算法
      'sp': '',
      'encoding': 'UTF-8',
      'prelt': '401',
      'rsakv': '',
      'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
      'returntype': 'META'
}
  
class WeiboLogin:
     def __init__(self, username, password):
          self.username = username
          self.password = password
      
     def __get_spwd(self):
          rsaPublickey = int(self.pubkey, 16)
          key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
          message = self.servertime + '\t' + self.nonce + '\n' + self.password #拼接明文js加密文件中得到
          passwd = rsa.encrypt(message, key) #加密
          passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
          return passwd
  
     def __get_suser(self):
         username_ = urllib.quote(self.username)
         username = base64.encodestring(username_)[:-1]
         return username
    
     def __prelogin(self):
          prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.4)' % self.username
          response = urllib2.urlopen(prelogin_url)
          p = re.compile(r'\((.*?)\)')
          strurl = p.search(response.read()).group(1)
          dic = dict(eval(strurl)) #json格式的response
          self.pubkey = str(dic.get('pubkey'))
          self.servertime = str(dic.get('servertime'))
          self.nonce = str(dic.get('nonce'))
          self.rsakv = str(dic.get('rsakv'))

     def login(self):
          url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
          try:
              self.__prelogin() #预登录
          except:
              print 'Prelogin Error'
              return
          global postdata
          postdata['servertime'] = self.servertime
          postdata['nonce'] = self.nonce
          postdata['su'] = self.__get_suser()
          postdata['sp'] = self.__get_spwd()
          postdata['rsakv'] = self.rsakv
          postdata = urllib.urlencode(postdata)
          headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0'}
          req  = urllib2.Request(
              url = url,
              data = postdata,
              headers = headers
          )
          result = urllib2.urlopen(req)
          text = result.read()
          p = re.compile('location\.replace\(\'(.*?)\'\)')
          try:
              login_url = p.search(text).group(1)
              urllib2.urlopen(login_url)
              print "Login Succeed!"
          except:
              print 'Login Error!'
