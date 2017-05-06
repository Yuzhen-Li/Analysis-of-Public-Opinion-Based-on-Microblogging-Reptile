# -*- coding: utf-8 -*-

#######对数据分析的结果画饼状图##################
import matplotlib.pyplot as plt
 
 
 
####招商银行服务相关微博情绪分析结果###
plt.figure(1)
labels = 'Positive', 'Negative'
sizes = [0.491148711441,0.508851291405]
colors = ['red', 'lightskyblue']
explode = (0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=90)
 
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
 
plt.title("Service - related microblogging emotional analysis")  

plt.savefig('E:\scrapy\\server.png')
plt.show()


####招商银行黑金卡相关微博情绪分析结果###
plt.figure(2)
labels = 'Positive', 'Negative'
sizes = [0.570161053113,0.429838944049]
colors = ['red', 'lightskyblue']
explode = (0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=90)
 
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
 
plt.title("Black_gold_card - related microblogging emotional analysis")  

plt.savefig('E:\scrapy\\Black_gold_card.png')
plt.show()


####招商银行信用卡相关微博情绪分析结果###
plt.figure(3)
labels = 'Positive', 'Negative'
sizes = [0.531730111206,0.468269890547]
colors = ['red', 'lightskyblue']
explode = (0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=90)
 
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
 
plt.title("Creditcard - related microblogging emotional analysis")  

plt.savefig('E:\scrapy\\Creditcard.png')
plt.show()

####招商银行手机银行相关微博情绪分析结果###
plt.figure(4)
labels = 'Positive', 'Negative'
sizes = [0.33999,0.66001]
colors = ['red', 'lightskyblue']
explode = (0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=90)
 
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
 
plt.title("Phone_bank - related microblogging emotional analysis")  

plt.savefig('E:\scrapy\\Phone_bank.png')
plt.show()


####招商银行一季度盈利额相关微博情绪分析结果###
plt.figure(5)
labels = 'Positive', 'Negative'
sizes = [0.669,0.331]
colors = ['red', 'lightskyblue']
explode = (0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=90)
 
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
 
plt.title("Profitability - related microblogging emotional analysis")  

plt.savefig('E:\scrapy\\Profitability.png')
plt.show()

####招商银行二维码支付相关微博情绪分析结果###
plt.figure(6)
labels = 'Positive', 'Negative'
sizes = [0.7302,0.2698]
colors = ['red', 'lightskyblue']
explode = (0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=90)
 
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
 
plt.title("Code_payment - related microblogging emotional analysis")  

plt.savefig('E:\scrapy\\Code_payment.png')
plt.show()



















