# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:23:21 2021

@author: Arthu
"""

from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage , ImageSendMessage , LocationSendMessage , VideoSendMessage
line_bot_api = LineBotApi('LLUIDJkmyavztyPBQh6fj0/8VgZJttwDCxyJT7f2PaSSpIXRy58REuFBjUBIRPdbxO+ySGHHxS7iw3qI9DCT/GX3cKiNhp7u07DollyCZN5jZ/gDAr1jH5z5AcMYpjSHCgXyBrdegy2oF/fIT4ihjgdB04t89/1O/w1cDnyilFU=')

UserID = 'U7ca47575b48d8f71700f5604113bbd68'

text_message = TextSendMessage(text = '1')
line_bot_api.push_message(UserID, text_message)
s = StickerSendMessage(package_id= '789' , sticker_id='10855')
line_bot_api.push_message(UserID, s)
image_message = ImageSendMessage(original_content_url='https://i.imgur.com/xyPtn4m.jpeg',preview_image_url='https://i.imgur.com/xyPtn4m.jpeg')
line_bot_api.push_message(UserID,image_message)
location_message = LocationSendMessage(
    title='CodingAPE猿創力程式設計學校',
    address='台北市信義區基隆路一段180號',
    latitude=25.042408,
    longitude=121.564839)
line_bot_api.push_message(UserID,location_message)
video_message = VideoSendMessage(
    original_content_url='https://i.imgur.com/oRcIXiM.mp4',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg'
)
line_bot_api.push_message(UserID,video_message)
