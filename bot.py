import nest_asyncio
#import time
#import os
import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot


'''
报错提示：
        如果go-cqhttp界面报错“监听反向WS API时出现错误”则是没有运行bot.py
        请及时更新go-cqhttp版本：https://github.com/Mrs4s/go-cqhttp/releases
        
相关提示：
        事件响应器的优先级代表事件响应器的执行顺序，同一优先级的事件响应器会 同时执行！
        优先级数字越小越先响应！优先级请从1开始排序！        

安装语音模块：
        setx /M PATH "H:\QQ_Bot_2021\ffmpeg-4.3.1-2021-01-01-full_build\ffmpeg-4.3.1-2021-01-01-full_build\bin;%PATH%"
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

'''
————————————————————————————————函数库————————————————————————————————
'''


# 启用异步线程
# !!!千万不能启用！！！#
# nest_asyncio.apply()
# nonebot通过.env.dev文件初始化
nonebot.init(_env_file=".env.dev")
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
# 加载nonebot内置插件
nonebot.load_builtin_plugins()
#加载一个"pip"安装的插件：Timer中的"nonebot_plugin_apscheduler"
nonebot.load_plugin("nonebot_plugin_apscheduler")
nonebot.load_plugin("nonebot_plugin_docs")
#nonebot.load_plugin("nonebot-tuling")
#加载本地的单独插件
#nonebot.load_plugin("awesome_bot.plugins.Gaming")
#nonebot.load_plugin("awesome_bot.plugins.The_Timer")
#加载插件目录，"awesome_bot/plugins"目录下为各插件，以下划线开头的插件将不会被加载
nonebot.load_plugins("awesome_bot/plugins")
#不加载插件目录时使用下面语句
#nonebot.load_builtin_plugins()

if __name__ == "__main__":
    nonebot.run()



