import requests
import json

def send_dingtalk_message(webhook_url, title, text, image_url=None):
    headers = {
        "Content-Type": "application/json"
    }

    # 构建富文本消息的数据结构
    message_data = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": f"#### {title}\n > {text}"
        }
    }

    # 如果有图片 URL，则添加图片
    if image_url:
        message_data["markdown"]["text"] += f"\n > ![图片]({image_url})"

    # 发送请求
    response = requests.post(webhook_url, headers=headers, data=json.dumps(message_data))

    if response.status_code == 200:
        print("消息发送成功")
    else:
        print(f"消息发送失败，状态码: {response.status_code}")

# 示例使用
webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=89f5ae934e92a4fc7e585bc705e95fc8fc586f0da51f4a1dc3ef1ce51bbd0c44"
title = "智能计量系统"
text = "智能计量系统历史数据"
image_url = "http://www.example.com/image.png"

send_dingtalk_message(webhook_url, title, text, image_url)