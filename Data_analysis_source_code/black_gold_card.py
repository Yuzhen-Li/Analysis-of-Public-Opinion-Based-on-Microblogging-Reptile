# -*- coding: utf-8 -*-

# 引入云API入口模块
from src.QcloudApi.qcloudapi import QcloudApi
import  xlrd
import  xlwt
import  re
import sys
import json
import requests
reload(sys)  
sys.setdefaultencoding('utf-8')  

#######情感分析，正面的，负面的情感

config = {
    'Region': 'gz',
    'secretId': 'AKIDwnUzIP76kCYnrvxcLwLrNkwypUSnuecQ',
    'secretKey': 'mMm05avAHOMvOflfQzLUTK0WsES4bwgK',
    'method': 'post'
}

#####计算情绪值的时候取平均值

def printpromotion(word):
	module = 'wenzhi'
	action = 'TextSentiment'
	service = QcloudApi(module, config)
	
	word=word.encode("utf-8")  ####编码
	#weburl='https://api.prprpr.me/emotion/wenzhi?password=DIYgod&text='+word
	params = {
        'content': word, #utf8 only
        'type': 4 #（可选参数，默认为4） 1：电商；2：APP；3：美食；4：酒店和其他。
    }
	#r = requests.get('%s' %weburl)
	json_str = json.loads(service.call(action, params))
	print "positive emotion:",(format(json_str["positive"],'0.1%'))
	print "negative emotion:",(format(json_str["negative"],'0.1%'))
	#ps = json_str["positive"]
	#ne = json_str["negative"]
	return json_str
	
    
	
	


data = xlrd.open_workbook(r'weiboData.xls') ##打开文件
rtable = data.sheets()[0]    ##获取sheet1
wbook = xlwt.Workbook(encoding='utf-8',style_compression = 0)  ##ncoding，设置字符编码，style_compression，表示是否压缩。这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。默认是ascii。
wtable = wbook.add_sheet('sheet2',cell_overwrite_ok = True)  ##新建一个Excel

servercount = 0
severpos = 0
serverneg = 0
avrseverpos = 0
avrserverneg = 0


##黑金卡  \u9ed1\u91d1\u5361

#####计算情绪值的时候取平均值
pattern = re.compile(u"(\u9ed1\u91d1\u5361)+")

for i in range(0,691):
	search = pattern.search(rtable.cell(i,7).value)
	if search:
		mood = printpromotion(rtable.cell(i,7).value)
		severpos = severpos + mood["positive"]
		serverneg = serverneg + mood["negative"]
		for j in range(0,8):
			wtable.write(i,j,rtable.row_values(i)[j])
		servercount +=1

print  u"和黑金卡有关的微博个数： ",servercount  #输出符合条件的行数
print  u"这些微博总得正面情绪: " ,severpos
print  u"这些微博总得负面情绪: " ,serverneg
avrseverpos = severpos / servercount
avrserverneg = serverneg /	servercount
print  u"平均正面情绪:",  avrseverpos
print  u"平均负面情绪:", avrserverneg
wbook.save(r'black_gold_card.xls')


#########################招商银行有哪些产品################

#########################信用卡##########################################################


























########################################手机银行######################################
















########################################招商银行在新加坡成立私人银行#########################################












########################招商银行支持银联二维码支付#####################################







#############一季度盈利额  度超过交行##########################







