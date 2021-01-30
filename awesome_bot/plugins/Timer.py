# -*- coding: utf-8 -*-
from nonebot import require


import nonebot
import socket
import os
import time




'''
The MIT License (MIT)

Copyright (c) 2021 Chancey Zhou

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''



'''
————————————————————————————————常量库————————————————————————————————
'''




'''
————————————————————————————————函数库————————————————————————————————
函数名称              功能              传入参数           返回值
isNetOK              是否已经联网       网址               T/F

'''

#——————————————————————————————————————————————————————————————
#是否已经联网
def isNetOk(testserver):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False
    
#——————————————————————————————————————————————————————————————
#

#——————————————————————————————————————————————————————————————
#
'''
————————————————————————————————功能库————————————————————————————————
名称                          事件响应器名称                     优先级

'''
#——————————————————————————————————————————————————————————————
#Mark_1
Mark_1 = require("nonebot_plugin_apscheduler").scheduler
@Mark_1.scheduled_job("cron", hour = "00", minute = "12", id = "Healthy_Information")
async def Mark_1_Reply():
    bot = nonebot.get_bots()['2336371525']
    isOK = isNetOk(('www.baidu.com',443))
    # add your code here!


#——————————————————————————————————————————————————————————————
#每秒测试任务
'''
Test = require("nonebot_plugin_apscheduler").scheduler

@Test.scheduled_job('cron', second = '*', id="Every_Second")
async def Test_Reply():
    bot = nonebot.get_bots()['2336371525']
    #私聊
    #await bot.send_msg(user_id = 1258691091,message = 'hello')

'''


#——————————————————————————————————————————————————————————————
#每分钟闹钟提醒任务
Mark_2 = require("nonebot_plugin_apscheduler").scheduler
@Mark_2.scheduled_job("cron", minute = '*', id = "Every_Minute")
async def Mark_2_Reply():
    bot = nonebot.get_bots()['2336371525']
    try:
        a = 1
    except:
        pass












