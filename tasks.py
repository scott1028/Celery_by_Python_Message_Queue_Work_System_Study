# coding:utf-8
#
# 以下展示 Celery with RabbitMQ 的 Message Queue 運作架構
# 最終運行的平台是 Worker Server, Client 只是傳遞 Task Message 過去而已，然後可以取回工作成果！
#
# 啟動 Worker Service 方式：
# Consumer:
#	celery -A task worker --loglevel=info
# Producer:
#	from tasks import *
#	echo.apply_async()		# or echo.delay()

from celery import Celery
import time,urllib2

app = Celery('hello',backend='amqp' , broker='amqp://guest@localhost//')

app.conf.update(
	# 建議使用原始的 pickle ，因為似乎JSON無法正確傳輸 Instance Object
    # CELERY_TASK_SERIALIZER='json',
    # CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    # CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Asia/Taipei',
    CELERY_ENABLE_UTC=True,
)

@app.task
def echo(string, string2=None):
	#print 'print %(string)d'%{'string':string}

	print '[MSG]',{'string':string}

	# time.sleep(3)

	for i in range(0,7):
		print string.__str__()+i.__str__()

	if string2!=None:
		return string.__str__()+','+string2.__str__()
	else:
		return string.__str__()

class Book(object):
	def __init__(self):
		self.x=100

@app.task
def getInstance():
	return Book()

@app.task
def requestURL():
	return urllib2.urlopen('http://www.youtube.com').read()
