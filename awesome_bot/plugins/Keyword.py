# -*- coding: utf-8 -*-
from nonebot import on_command, on_keyword, on_startswith, on_endswith
#from nonebot import on_request,on_notice
#from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event#, MessageSegment
#from nonebot.notice_request import RequestSession
import random
import socket
import requests
import json

'''
报错提示：
        
相关提示：
        在“baby唤醒”功能中的唤醒词如果与配置“.env.dev”文件中机器人昵称有重复，则机器人不会响应。
'''


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
URL_KUA         = 'https://chp.shadiao.app/api.php'
URL_TRANSLATE   = 'http://fanyi.youdao.com/translate'  
URL_MUSIC       = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?aggr=1&cr=1&flag_qc=0&p=1&n=1&w='
URL_BAIKE       = 'https://baike.baidu.com/item/'
URL_MOVIE_ID    = 'https://movie.douban.com/j/subject_suggest?q='
URL_DOUBAN      = 'https://movie.douban.com/subject/'
URL_JOKE        = 'http://new.toodo.fun/apis'
URL_Zuan        = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_ch'

'''
————————————————————————————————函数库————————————————————————————————
函数名称              功能                  传入参数           返回值
isNetOK              是否已经联网           网址               T/F
ifNetBroken          断网发送内容选择器      \                 机器人回复的话
Mid_String           取字符串中指定字符串    整体字符串          目标字符串

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
#断网发送内容选择器
def ifNetBroken():
    a = random.randint(1,3)
    if a == 1:
        return '哎呀！(x_x)谁拔我网线？'
    elif a == 2:
        return '啊……我感觉……好热……啊！(x_x)'
    else:
        return '我去世了……（安详 x_x'


#——————————————————————————————————————————————————————————————
#取字符串中指定字符串
def Mid_String(content,startStr,endStr):                     
    startIndex = content.index(startStr)                    
    if startIndex>=0:                                       
        startIndex += len(startStr)                         
        endIndex = content.index(endStr)                    
        return content[startIndex:endIndex]                 



'''
————————————————————————————————功能库————————————————————————————————
名称                          事件响应器名称                     优先级


'''

'''
事件响应器类型 type
事件响应器类型其实就是对应事件的类型 Event.get_type()NoneBot提供了一个基础类型事件响应器on()以及一些其他内置的事件响应器。
以下所有类型的事件响应器都是由 on(type, rule) 的形式进行了简化封装。
on("事件类型"): 基础事件响应器，第一个参数为事件类型，空字符串表示不限
[]on_metaevent() ~ on("meta_event"): 元事件响应器
[]on_message() ~ on("message"): 消息事件响应器
[]on_request() ~ on("request"): 请求事件响应器
[]on_notice() ~ on("notice"): 通知事件响应器
[√]on_startswith(str) ~ on("message", startswith(str)): 消息开头匹配响应器，参考 startswith
[√]on_endswith(str) ~ on("message", endswith(str)): 消息结尾匹配响应器，参考 endswith
[√]on_keyword(set) ~ on("message", keyword(str)): 消息关键词匹配响应器，参考 keyword
[√]on_command(str|tuple) ~ on("message", command(str|tuple)): 命令响应器，参考 command
[]on_regex(pattern_str) ~ on("message", regex(pattern_str)): 正则匹配处理器，参考 regex

'''

#——————————————————————————————————————————————————————————————
#keyword
X_1 = on_keyword(keywords = ['keyword'], priority = 1)
@X_1.handle()
async def X_1_Reply(bot: Bot, event: Event, state: dict):
    await bot.send(
                    event = event,
                    message = '这是KeyWord的回复！' + '\n' + str(event.message)
                    )

#——————————————————————————————————————————————————————————————
#command
X_2 = on_command('command', priority = 1)
@X_2.handle()
async def X_2_Reply(bot: Bot, event: Event, state: dict):
    await bot.send(
                    event = event,
                    message = '这是Command的回复！' + '\n' + str(event.message)
                    )
   
#——————————————————————————————————————————————————————————————
#startswith
X_3 = on_startswith('startwith',priority = 1)        
@X_3.handle()
async def X_3_Reply(bot: Bot, event: Event, state: dict):
    await bot.send(
                    event = event,
                    message = '这是startswith的回复！' + '\n' + str(event.message)
                    )

#——————————————————————————————————————————————————————————————
#endswith
X_4 = on_endswith('endwith',priority = 1)        
@X_4.handle()
async def X_4_Reply(bot: Bot, event: Event, state: dict):
    await bot.send(
                    event = event,
                    message = '这是endwith的回复！' + '\n' + str(event.message)
                    )
'''
#——————————————————————————————————————————————————————————————
#notice
X_5 = on_notice()        
@X_5.handle()
async def X_5_Reply(bot: Bot, event: Event, state: dict):
    await bot.send(
                    event = event,
                    message = '收到通知' #+ '\n' + str(event.message)
                    )

'''



cfop = on_command("picture", priority=1)
@cfop.handle()
async def cfopsend(bot: Bot, event: Event, state: dict):
    '''
        message = '[CQ:image,file=9d68078d5880e8acaa71e0c9c1ebac07.image,url=http://c2cpicdw.qpic.cn/offpic_new/2637087493//2637087493-601208238-9D68078D5880E8ACAA71E0C9C1EBAC07/0?term=2]'
    

    '''
    await bot.send(
        event=event,
        message = '[CQ:image,file=9d68078d5880e8acaa71e0c9c1ebac07.image,url=http://c2cpicdw.qpic.cn/offpic_new/2637087493//2637087493-601208238-9D68078D5880E8ACAA71E0C9C1EBAC07/0?term=2]'
    )
#--------------------------------------------娱乐功能--------------------------------------------#
#点歌√
Share_Music = on_command('点歌', priority = 2)
@Share_Music.handle()
async def Share_Music_Reply(bot: Bot, event: Event, state: dict):
    isOK = isNetOk(('www.baidu.com',443))
    if  isOK :
        if str(event.message):
            Song_url = URL_MUSIC + str(event.message)
            data_text = requests.get(Song_url).text
            data_json = json.loads(data_text[9:-1])
            SongID = data_json["data"]["song"]["list"][0]["songid"]
            await bot.send(
                            event = event,
                            message = '[CQ:music,type=qq,id=%d,]'%SongID
                            )
        else:
            await bot.send(
                            event = event,
                            message = '[错误]格式：点歌好运来',
                            at_sender = True
                            )
    else:
        await bot.send(
                        event = event,
                        message = ifNetBroken()
                        )
#戳一戳√
Chuo_chuo = on_keyword(keywords = {'戳我','捏我','拍我'}, priority = 3)
@Chuo_chuo.handle()
async def Chuo_chuo_Reply(bot: Bot, event: Event, state: dict):
    #确保消息来源于群组
    if event.group_id != None:
        await bot.send(
                        event =   event,
                        message = '[CQ:poke,qq=%s]'%(str(event.user_id))
                       )
       
#送免费礼物√
Give_Present = on_keyword(keywords = {'礼物'}, priority = 4)
@Give_Present.handle()
async def Give_Present_Reply(bot: Bot, event: Event, state: dict):
    #确保消息来源于群组
    if event.group_id != None:
        a = random.randint(0,13)
        if event.user_id == 1258691091 :
            await bot.send(
                            event =   event,
                            message = '[CQ:gift,qq=%s,id=%d]'%(str(event.user_id),a)
                           )
        else:
            await bot.send(
                            event =   event,
                            message = '你送我一个我就给你！'
                           )

#文本转语音√
To_voice = on_command('说', priority = 5)
@To_voice.handle()
async def To_voice_Reply(bot: Bot, event: Event, state: dict):
    #确保消息来源于群组
    if event.group_id != None:     
        TXT = str(event.message)
        if event.user_id == 1258691091 :
            await bot.send(
                             event =   event,
                             message = '[CQ:tts,text=%s]'%TXT
                            )
        else:
            probability = random.randint(1,280)
            if probability < 60 :
                await bot.send(
                                event =   event,
                                message = '不发！'
                               )
            elif probability >= 60 and  probability <= 90 :
                await bot.send(
                                 event =   event,
                                 message = '[CQ:tts,text=%s]'%TXT
                                )
            else:
                await bot.send(
                                event =   event,
                                message = '我嗓子疼了，想听我说话，给我送礼物吧~'
                               )
     















