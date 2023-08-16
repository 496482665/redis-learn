# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/8 16:00
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => steam_class.py
"""
from redis import Redis

from core.base import BaseDataType


# =========================== #
#      操作redis的stream功能
# =========================== #
class Stream(BaseDataType):
    """
    xadd(name, fields, , id="", maxlen=None, approximate=True) - 向Stream中添加一个事件
    xdel(name, *ids) - 从Stream中删除一个或多个事件
    xgroup_create(name, groupname, id="0", mkstream=False) - 创建一个消费者组
    xgroup_setid(name, groupname, id) - 设置消费者组的偏移量
    xgroup_destroy(name, groupname) - 销毁一个消费者组
    xgroup_delconsumer(name, groupname, consumername) - 从消费者组中删除一个消费者
    xlen(name) - 获取Stream中的事件数量
    xrange(name, start="-", end="+", count=None) - 获取指定范围内的事件
    xread(streams, count=None, block=None) - 读取指定Stream的事件
    xreadgroup(groupname, consumername, streams, count=None, block=None, noack=False) - 以组的方式读取指定Stream的事件
    xack(name, groupname, *ids) - 确认消费者组已经处理了指定的事件
    xclaim(name, groupname, consumername, min_idle_time, *ids, idle=None, time=None, retrycount=None, force=False) - 将事件从一个消费者组的待处理列表移动到另一个消费者组
    xinfo_stream(name) - 获取Stream的信息
    xinfo_groups(name) - 获取Stream的消费者组信息
    xinfo_consumers(name, groupname) - 获取消费者组的消费者信息
    xpending(name, groupname) - 获取消费者组的待处理事件信息
    xpending_range(name, groupname, start, end, count=None, consumername=None) - 获取指定范围内的待处理事件信息
    xtrim(name, maxlen, approximate=True) - 修剪Stream，保留指定数量的事件
    """
    def handle(self, client: Redis):
        # xadd(name, fields, id=b'*', maxlen=None, approximate=True): 向Stream中添加一条消息
        message_id = client.xadd('mystream', {'name': 'Alice', 'age': 30})
        print("Added message with ID:", message_id)

        # xlen(name): 获取Stream中的消息数量
        stream_length = client.xlen('mystream')
        print("Stream length:", stream_length)

        # xread(streams, count=None, block=None, group=None, consumer=None, latest_ids=None): 从一个或多个Stream中读取消息
        # messages = client.xread({'mystream': '$'}, count=1, block=0)
        # print("Read messages:", messages)

        # xgroup_create(name, stream, id, mkstream=False): 创建一个消费者组
        groups = [group.get("name") for group in client.xinfo_groups("mystream")]
        print(groups)
        if b"mygroup" not in groups:
            group_created = client.xgroup_create('mystream', 'mygroup', id='$', mkstream=True)
            print("Group created:", group_created)

        # xrange(name, start="-", end="+", count=None) - 获取指定范围内的事
        stream_messages = client.xrange("mystream", "-", "+", count=100)
        print("Read group messages:", stream_messages)

        # xreadgroup(groupname, consumername, streams, count=None, block=None, noack=False, latest_ids=None): 从消费者组中读取消息
        group_messages = client.xreadgroup('mygroup', 'consumer1', {'mystream': '>'}, count=1, block=0, noack=False)
        print("Read group messages:", group_messages)

        # xack(name, groupname, *ids): 确认消费者组已处理的消息
        client.xack('mystream', 'mygroup', message_id)

        # xpending(name, groupname): 获取消费者组中待处理的消息信息
        pending_info = client.xpending('mystream', 'mygroup')
        print("Pending info:", pending_info)

        # xclaim(name, groupname, consumername, min_idle_time, message_ids, idle=None, time=None, retrycount=None, force=False): 尝试重新分配未确认的消息给指定的消费者
        claimed_messages = client.xclaim('mystream', 'mygroup', 'consumer1', 10000, [message_id])
        print("Claimed messages:", claimed_messages)

        # xinfo_stream(name): 获取Stream的信息
        stream_info = client.xinfo_stream('mystream')
        print("Stream info:", stream_info)

        # xinfo_groups(name): 获取Stream中消费者组的信息
        group_info = client.xinfo_groups('mystream')
        print("Group info:", group_info)

        # xinfo_consumers(name, groupname): 获取消费者组中消费者的信息
        consumer_info = client.xinfo_consumers('mystream', 'mygroup')
        print("Consumer info:", consumer_info)
