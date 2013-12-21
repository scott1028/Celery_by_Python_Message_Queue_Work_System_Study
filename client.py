# coding:utf-8
# 
# When this module is executed the tasks will be named starting with “__main__”,
# but when the module is imported by another process, say to call a task,
# the tasks will be named starting with “tasks”.
# 
# 參考：http://docs.celeryproject.org/en/master/userguide/application.html
#
# worker task 必須使用引用
from tasks import *

t=[]
for i in range(0,10):
	c=echo.apply_async(['testA'],countdown=3)
	t.append(c)

for st in t:
	print c.get()