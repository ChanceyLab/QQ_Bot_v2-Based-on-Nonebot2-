# -*- coding: utf-8 -*-
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
from nonebot import on_notice

import random
import socket

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
函数名称              功能                  传入参数           返回值
isNetOK              是否已经联网           网址               T/F
ifNetBroken          断网发送内容选择器      \                 机器人回复的话
Mid_String           取字符串中指定字符串    整体字符串          目标字符串

'''


# ——————————————————————————————————————————————————————————————
# 是否已经联网
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


# ——————————————————————————————————————————————————————————————
# 断网发送内容选择器
def ifNetBroken():
    a = random.randint(1 ,3)
    if a == 1:
        return '哎呀！(x_x)谁拔我网线？'
    elif a == 2:
        return '啊……我感觉……好热……啊！(x_x)'
    else:
        return '我去世了……（安详 x_x'


# ——————————————————————————————————————————————————————————————
# 取字符串中指定字符串
def Mid_String(content ,startStr ,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
        endIndex = content.index(endStr)
        return content[startIndex:endIndex]



'''
————————————————————————————————功能库————————————————————————————————
名称                          事件响应器名称                     优先级
新人入群                        group_increase                   2


'''







# 注册事件响应器, 新增群成员
group_increase = on_notice(priority=2)
@group_increase.handle()
async def handle_group_increase(bot: Bot, event: Event, state: dict):
    user_id = event.dict().get('user_id')
    group_id = event.dict().get('group_id')
    detail_type = event.dict().get(f'{event.get_type()}_type')
    if detail_type == 'group_increase' :
        at_seg = MessageSegment.at(user_id=user_id)
        msg = f'来人啊！快欢迎新朋友进群~\n想知道我的用法可以发送“功能”\n{at_seg}'
        await bot.send(event=event, message=Message(msg))
