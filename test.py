# coding:utf-8

# worker task 必須使用引用
from tasks import *

t=[]
for i in range(0,10):
	c=echo.apply_async(['testA'],countdown=3)
	t.append(c)

for st in t:
	print c.get()