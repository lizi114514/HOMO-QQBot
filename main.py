import botpy
import aiohttp
import random
from botpy.message import GroupMessage
from dotenv import load_dotenv
from botpy.ext.command_util import Commands
from botpy.types.message import Ark, ArkKv
from botpy import BotAPI
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 读取配置
bot_app_id = os.getenv("APP_ID")
bot_app_secret = os.getenv("APP_SECRET")
print(bot_app_secret)
print(bot_app_id)
# 验证是否读取成功
if not bot_app_id or not bot_app_secret:
    raise ValueError("请在 .env 文件中正确配置 APP_ID 和 APP_SECRET")

print(f"成功读取 AppID: {bot_app_id}")
print(f"成功读取 AppSecret: {bot_app_secret}") # 注意：真实项目中切勿打印完整Secret

#######定义commands类型############

@Commands("/help")
async def cmd_help(api: BotAPI, message: GroupMessage, params=None):
    """处理 /help 指令"""
    help_text = (
        "可用指令：\n"
        "/help 显示帮助\n"
        "/echo <内容> 复述内容\n"
        "/time 显示当前时间"
    )
    await message.reply(content=help_text)
    return True  # 返回 True 表示指令已被处理，停止后续匹配

@Commands("/echo")
async def cmd_echo(api: BotAPI, message: GroupMessage, params=None):
    """处理 /echo 指令，params 是 /echo 后面的文本"""
    if not params:
        await message.reply(content="请在 /echo 后面输入要复述的内容。")
    else:
        await message.reply(content=f"你说：{params}")
    return True

@Commands("/time")
async def cmd_time(api: BotAPI, message: GroupMessage, params=None):
    """处理 /time 指令"""
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await message.reply(content=f"当前时间：{now}")
    return True

@Commands("/sese")
async def cmd_sese(api: BotAPI, message: GroupMessage, params=None):
    """处理 /sese 指令"""
    sese = "不...不能色色😭，API已经被调得破烂不堪了😵‍💫"
    await message.reply(content=sese)
    return True

@Commands("/你是谁")
async def cmd_whoru(api: BotAPI, message: GroupMessage, params=None):
    """处理 /你是谁 指令"""
    whoru_text = (
        "今年24岁\n"
        "是一个一个一个学生\n"
        "在群里迷茫的看着众人\n"
        "不知道今天中午吃什么（绝对不是雪啊 囧"
    )
    await message.reply(content=whoru_text)
    return True  # 返回 True 表示指令已被处理，停止后续匹配

############Command类型定义结束############





class MyClient(botpy.Client):
    async def on_group_at_message_create(self, message: GroupMessage): 
        print(message.content)
        #await message.reply(content=f"机器人{self.robot.name}收到你的@消息了: {message.content}")
        handlers = [cmd_help, cmd_echo, cmd_time, cmd_sese, cmd_whoru]
        for handler in handlers:
            if await handler(api=self.api, message=message):
                return
        await message.reply(content="未知指令，发送 /help 查看可用指令。")
intents = botpy.Intents(public_messages=True) 
client = MyClient(intents=intents)
client.run(appid=bot_app_id, secret=bot_app_secret)