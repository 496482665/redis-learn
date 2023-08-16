# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/15 16:04
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => pub_sub.py
"""
from redis import Redis
import time
import threading


# =========================== #
#      操作redis的 发布-订阅 功能
# =========================== #
# 创建一个发布者类
class Publisher(threading.Thread):
    def __init__(self, name, r: Redis, channel):
        super().__init__(name=name)
        self.r = r
        self.channel = channel

    def publish(self):
        count = 0
        # 发布消息
        while True:
            message = f"channel message:{count}"
            self.r.publish(self.channel, message)
            count += 1
            time.sleep(3)

    def run(self) -> None:
        self.publish()


# 创建一个订阅者类
class Subscriber(threading.Thread):
    def __init__(self, r: Redis, channels):
        super().__init__()
        self.pubsub = r.pubsub()
        self.pubsub.subscribe(channels)
        # self.pubsub.subscribe("channel1","channel2") # 同时订阅多个频道
        # self.pubsub.psubscribe("channel1*") # 以通配符形式同时订阅多个频道
        # self.pubsub.punsubscribe("channel1*") # 以通配符形式同时取消订阅多个频道
        # self.pubsub.unsubscribe(channels) # 取消订阅

    def run(self):
        for message in self.pubsub.listen():
            # 处理接收到的消息
            print(f"Received message: {message['data']}")
            # 在这里你可以根据具体需求来处理消息


def start(r):
    channel = "channel1"

    # 一个发布者
    publish = Publisher(name="pub_thread", r=r, channel=channel)
    publish.start()

    # 两个订阅者
    sub1 = Subscriber(r, channel)
    sub2 = Subscriber(r, channel)
    sub1.start()
    sub2.start()
