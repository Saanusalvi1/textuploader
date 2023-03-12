from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import tgcrypto
from p_bar import progress_bar
#from details import api_id, api_hash, bot_token
from subprocess import getstatusoutput
import helper
import logging
import time
import glob
import aiohttp
import asyncio
import aiofiles
from pyrogram.types import User, Message
# import progressor
# from progressor import progress_for_pyrogram
#import sys
import re
import os
import io
#import pycurl

# bot = Client(
#     "bot",
#     api_id=api_id,
#     api_hash=api_hash,
#     bot_token=bot_token)

bot = Client(
    "bot",
    bot_token= "5659489542:AAGFjU4zc6fAasB4x1arOOqqOWpTpTCUe5M",
    api_id= "27005191",
    api_hash= "25f3ca5a50a9eacee7c19441222d14c2"
)

logger = logging.getLogger()

os.makedirs("./downloads", exist_ok=True)

@bot.on_message(filters.command(["start"])& ~filters.edited)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Hello im txt file downloader\nPress /pyro to download links listed in a txt file in the format Name:link\nBot made by DRAGO")




keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Devloper",
                url="https://pornhub.com/",
            ),
            InlineKeyboardButton(
                text="Repo",
                url="https://lund-chushLoo.com/repo",
            ),
        ],
    ]
)


@bot.on_message(filters.command(["pyro"]))
async def account_login(bot: Client, m: Message):

 editable = await m.reply_text("**Hi Press**\n**Text** = /pro_txt\n**Top** = /pro_top\n**Vision** = /pro_vision\n**Jw** = /pro_jw\n**Olive** = /pro_olive\n**Addapdf** = /adda_pdf")


@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait\n🚦🚦 Last Process Stopped 🚦🚦")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return


@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["pro_txt"]))
async def account_login(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    if user is not None and user not in sudo_users:
        await m.reply("**bhag bhosadi ke", quote=True)
        return
    else:
        editable = await m.reply_text(
            "Hello Bruh **I am Text Downloader Bot**. I can download videos from **text** file one by one.**\n\nDeveloper** : NAAM TO SUNA HOGA**\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File {Name : Link}")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4 = await m.reply_text(
        "Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()

            if raw_text2 == "144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data1 in out:
                        ytf = out[data1]
            elif raw_text2 == "180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data2 in out:
                        ytf = out[data2]
            elif raw_text2 == "240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data3 in out:
                        ytf = out[data3]
            elif raw_text2 == "360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']
                elif '1280x720' in out:
                    ytf = out['1280x720']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data4 in out:
                        ytf = out[data4]
            elif raw_text2 == "480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['854x470']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf = ['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data5 in out:
                        ytf = out[data5]

            elif raw_text2 == "720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '1280x720' in out:
                    ytf = out['1280x720']
                elif '1280x704' in out:
                    ytf = out['1280x704']
                elif '1280x474' in out:
                    ytf = out['1280x474']
                elif '1920x712' in out:
                    ytf = out['1920x712']
                elif '1920x1056' in out:
                    ytf = out['1920x1056']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    fo
