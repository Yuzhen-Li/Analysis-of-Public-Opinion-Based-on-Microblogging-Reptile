# coding: utf-8

__author__ = 'Zhang Huajian'

'''
以关键词收集新浪微博
'''
import wx
import sys
import urllib
import urllib2
import re
import json
import hashlib
import os
import time
from datetime import datetime
from datetime import timedelta
import random
from lxml import etree
import logging
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime


class CollectData():
    """数据收集类
       利用微博高级搜索功能，按关键字搜集一定时间范围内的微博。
    """
    def __init__(self, keyword, startTime, interval='50', flag=True, begin_url_per = "http://s.weibo.com/weibo/"):
        self.begin_url_per = begin_url_per  #设置固定地址部分，默认为"http://s.weibo.com/weibo/"
        self.setKeyword(keyword)    #设置关键字
        self.setStartTimescope(startTime)   #设置搜索的开始时间
        #self.setRegion(region)  #设置搜索区域
        self.setInterval(interval)  #设置邻近网页请求之间的基础时间间隔（注意：过于频繁会被认为是机器人）
        self.setFlag(flag)  #设置
        self.logger = logging.getLogger('main.CollectData') #初始化日志

    ##设置关键字
    ##关键字需解码
    def setKeyword(self, keyword):
        self.keyword = keyword.decode('GBK').encode("utf-8") #先将其GBK解码，然后再UTF-8编码，然后再输出：
        print 'twice encode:',self.getKeyWord()

    ##设置起始范围，间隔为1天
    ##格式为：yyyy-mm-dd
    def setStartTimescope(self, startTime):
        if not (startTime == '-'):
            self.timescope = startTime + ":" + startTime
        else:
            self.timescope = '-'

    ##设置搜索地区
    #def setRegion(self, region):
    #    self.region = region

    ##设置邻近网页请求之间的基础时间间隔
    def setInterval(self, interval):
        self.interval = int(interval)

    ##设置是否被认为机器人的标志。若为False，需要进入页面，手动输入验证码
    def setFlag(self, flag):
        self.flag = flag

    ##构建URL
    def getURL(self):
        return self.begin_url_per+self.getKeyWord()+"&typeall=1&suball=1&timescope=custom:"+self.timescope+"&page="
     ##固定地址+关键字二次UTF-8编码+
     ##http://s.weibo.com/weibo/%25E8%2583%2596%25E7%25BA%25B8%25E5%2592%258C%25E7%2598%25A6%25E7%25BA%25B8%25E7
	 ##%259A%2584%25E5%258C%25BA%25E5%2588%25AB&typeall=1&suball=1&timescope=custom:2017-05-01-0:2017-05-02-0&Refer=g
    ##关键字需要进行两次urlencode
    def getKeyWord(self):
        once = urllib.urlencode({"kw":self.keyword})[3:]  #首先把中文字符转换为十六进制，然后在每个字符前面加一个标识符%。
        return urllib.urlencode({"kw":once})[3:]

    ##爬取一次请求中的所有网页，最多返回50页
    def download(self, url, maxTryNum=4):
        hasMore = True  #某次请求可能少于50页，设置标记，判断是否还有下一页
        isCaught = False    #某次请求被认为是机器人，设置标记，判断是否被抓住。抓住后，需要复制log中的文件，进入页面，输入验证码
        name_filter = set([])    #过滤重复的微博ID  set 一个无序不重复元素集
        
        i = 1   #记录本次请求所返回的页数
        while hasMore and i < 51 and (not isCaught):    #最多返回50页，对每页进行解析，并写入结果文件
            source_url = url + str(i)   #构建某页的URL  在原来的基础上加上page后面的页码
            data = ''   #存储该页的网页数据
            goon = True #网络中断标记
            ##网络不好的情况，试着尝试请求三次
            for tryNum in range(maxTryNum): ##0-3
                try:
                    html = urllib2.urlopen(source_url, timeout=12)
                    data = html.read()
                    break
                except:
                    if tryNum < (maxTryNum-1):
                        time.sleep(10)
                    else:
                        print 'Internet Connect Error!'
                        self.logger.error('Internet Connect Error!')
                        self.logger.info('url: ' + source_url)
                        self.logger.info('fileNum: ' + str(fileNum))
                        self.logger.info('page: ' + str(i))
                        self.flag = False
                        goon = False
                        break
            if goon:
                lines = data.splitlines()   ##按照行分隔，返回一个包含各行作为元素的列表
                isCaught = True
                for line in lines:
                    ## 判断是否有微博内容，出现这一行，则说明没有被认为是机器人
                    if line.startswith('<script>STK && STK.pageletM && STK.pageletM.view({"pid":"pl_weibo_direct"'):  ##判断字符串以   开头，此处是微博页面代码
                        isCaught = False
                        n = line.find('html":"')  ##返回html在该行的索引值
                        if n > 0:
                            j = line[n + 7: -11].encode("utf-8").decode('unicode_escape').encode("utf-8").replace("\\", "")
                            ## 没有更多结果页面
                            if (j.find('<div class="search_noresult">') > 0):
                                hasMore = False
                            ## 有结果的页面
                            else:
                                #此处j要decode！
                                page = etree.HTML(j.decode('utf-8'))
                                ps1 = page.xpath("//p[@node-type='feed_list_content']")   #使用xpath解析得到微博内容
                                as2 = page.xpath("//a[@class='W_texta W_fb']")   #使用xpath解析得到博主地址
                                ai = 0
                                #获取昵称和微博内容
                                for p1 in ps1:
                                    name = p1.attrib.get('nick-name')
                                    txt = p1.xpath('string(.)')
                                    addr1 = as2[ai].attrib.get('href')
                                    u = addr1.find('u/')
                                    addr = ''
                                    if u > 0:
                                        addr = addr1.replace("u/","p/100505") + '/info?mod=pedit_more'
                                    else:
                                        addr = addr1 + '/info?mod=pedit_more'  #获得博主个人信息地址
                                    locate = ''
                                    sex = ''
                                    edu = ''
                                    ai += 1
                                    data2 = ''   #存储该页的网页数据
                                    html2 = urllib2.urlopen(addr, timeout=12)
                                    data2 = html2.read()
                                    lines2 = data2.splitlines()
                                    for line2 in lines2:
                                        if line2.startswith('<script>FM.view({"ns":"","domid":"Pl_Official_PersonalInfo__59","css":["style/css/module/pagecard/PCD_text_b.css?version=97033aed3c17bc3f"]'):
                                            n2 = line2.find('html":"')
                                            if n2 > 0:
                                                j2 = line2[n2 + 7: -12].replace("\\", "")
                                                page2 = etree.HTML(j2.decode('utf-8'))
                                                infotype1 = u'所在地：'
                                                infotype2 = u'性别：'
                                                infotype3 = u'小学：'
                                                infotype4 = u'初中：'
                                                infotype5 = u'高中：'
                                                infotype6 = u'大学：'
                                                infotype = ''
                                                info = ''
                                                ps2 = page2.xpath("//span[@class = 'pt_title S_txt2']")
                                                info = page2.xpath("//span[@class = 'pt_detail']")
                                                infoIndex = 0
                                                for p2 in ps2:
                                                    infotype = p2.xpath('string(.)')
                                                    if (infotype == infotype1):
                                                        locate = info[infoIndex].xpath('string(.)')
                                                    if (infotype == infotype2):
                                                        sex = info[infoIndex].xpath('string(.)')
                                                    if (infotype == infotype3 or infotype == infotype4 or infotype == infotype5 or infotype == infotype6):
                                                        edu = infotype.replace("：","")
                                                        break
                                                    infoIndex += 1
                                    if(name != 'None' and str(txt) != 'None' and name not in name_filter):
                                        name_filter.add(name)
                                        oldWb = xlrd.open_workbook('weiboData.xls', formatting_info=True)
                                        oldWs = oldWb.sheet_by_index(0)
                                        rows = int(oldWs.cell(0,0).value)
                                        newWb = copy(oldWb)
                                        newWs = newWb.get_sheet(0)
                                        newWs.write(rows, 0, str(rows))
                                        newWs.write(rows, 1, name)
                                        newWs.write(rows, 2, locate)
                                        newWs.write(rows, 3, sex)
                                        newWs.write(rows, 4, edu)
                                        newWs.write(rows, 5, self.timescope)
                                        newWs.write(rows, 6, addr1)
                                        newWs.write(rows, 7, txt)
                                        newWs.write(0, 0, str(rows+1))
                                        newWb.save('weiboData.xls')
                                        print "save with same name ok"
                        break
                lines = None
                ## 处理被认为是机器人的情况
                if isCaught:
                    print 'Be Caught!'
                    self.logger.error('Be Caught Error!')
                    self.logger.info('url: ' + source_url)
                    self.logger.info('fileNum: ' + str(fileNum))
                    self.logger.info('page:' + str(i))
                    data = None
                    self.flag = False
                    break
                ## 没有更多结果，结束该次请求，跳到下一个请求
                if not hasMore:
                    print 'No More Results!'
                    if i == 1:
                        time.sleep(random.randint(3,8))
                    else:
                        time.sleep(10)
                    data = None
                    break
                i += 1
                ## 设置两个邻近URL请求之间的随机休眠时间，防止Be Caught。目前没有模拟登陆
                sleeptime_one = random.randint(self.interval-25,self.interval-15)
                sleeptime_two = random.randint(self.interval-15,self.interval)
                if i%2 == 0:
                    sleeptime = sleeptime_two
                else:
                    sleeptime = sleeptime_one
                print 'sleeping ' + str(sleeptime) + ' seconds...'
                time.sleep(sleeptime)
            else:
                break
        #content.close()
        #content = None

    ##改变搜索的时间范围，有利于获取最多的数据   
    def getTimescope(self, perTimescope):
        if not (perTimescope=='-'):
            times_list = perTimescope.split(':')
            start_date =  datetime(int(times_list[-1][0:4]),  int(times_list[-1][5:7]), int(times_list[-1][8:10]) ) 
            #start_date = datetime.date.fromtimestamp(time.mktime(time.strptime(times_list[-1],"%Y-%m-%d")))
            start_new_date = start_date - timedelta(days = 1)   ##从当前时间开始减1天
            start_str = start_new_date.strftime("%Y-%m-%d")   ##接收以时间元组，并返回以可读字符串表示的当地时间
            return start_str + ":" + start_str
        else:
            return '-'

def main():
    logger = logging.getLogger('main')  #获得日志系统的  对象，即创建一个logger
    logFile = './collect.log'
    logger.setLevel(logging.DEBUG)      #设置日志级别 NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
    filehandler = logging.FileHandler(logFile)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    filehandler.setFormatter(formatter)   
    logger.addHandler(filehandler)


    while True:
        ## 接受键盘输入
        keyword = raw_input('Enter the keyword(type \'quit\' to exit ):')
        if keyword == 'quit':
            sys.exit()
        startTime = raw_input('Enter the start time(Format:YYYY-mm-dd):')
        Ndays = int(raw_input('Enter the recent N days messages:'))
        #region = raw_input('Enter the region([BJ]11:1000,[SH]31:1000,[GZ]44:1,[CD]51:1):')
        #interval = raw_input('Enter the time interval( >30 and deafult:50):')
        mmm = 0  #计数天数
        ##实例化收集类，收集指定关键字和起始时间的微博
        cd = CollectData(keyword, startTime)
        while cd.flag:
            if mmm == Ndays:
                print "Have finished all messages!"
                sys.exit()
            print cd.timescope
            logger.info(cd.timescope)   ##打印日志信息
            url = cd.getURL()   ##获取URL符合新浪高级搜索的URL结构
            cd.download(url)
            cd.timescope = cd.getTimescope(cd.timescope)  #改变搜索的时间，到下一天
            mmm += 1
        else:
            cd = None
            print '-----------------------------------------------------'
            print '-----------------------------------------------------'
    else:
        logger.removeHandler(filehandler)
        logger = None
##if __name__ == '__main__':
##    main()
