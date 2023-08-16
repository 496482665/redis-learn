# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/7 18:00
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => list_class.py
"""
from redis import Redis

from core.base import BaseDataType


# =========================== #
#      操作redis的list功能
# =========================== #
# Redis中的List是一种有序的字符串列表数据结构。
# 它可以在列表的两端（头部和尾部）进行快速的插入和删除操作，因此非常适合用于实现队列、栈和消息队列等场景。
# List本质上是一个双向链表，并且使用跳表来提高性能和效率。
class List(BaseDataType):
    """
    lpush(name, *values): 将一个或多个值插入到列表的左侧（头部）。
    rpush(name, *values): 将一个或多个值插入到列表的右侧（尾部）。
    lrange(name, start, end): 获取列表中指定范围内的元素。
    lindex(name, index): 获取列表中指定索引位置的元素。
    llen(name): 获取列表的长度（元素个数）。
    lpop(name): 移除并返回列表的左侧（头部）元素。
    rpop(name): 移除并返回列表的右侧（尾部）元素。
    lrem(name, num=0, value): 从列表中移除指定值的元素。
    lset(name, index, value): 将列表中指定索引位置的元素设置为指定值。
    ltrim(name, start, end): 保留列表中指定范围内的元素，移除其他元素。
    rpoplpush(src, dst): 将一个列表的右侧（尾部）元素移动到另一个列表的左侧（头部）。
    """

    def handle(self, r: Redis):
        # lpush(name, *values)示例
        r.lpush('mylist', 'value1')
        r.lpush('mylist', 'value2', 'value3')

        # rpush(name, *values)示例
        r.rpush('mylist', 'value4')
        r.rpush('mylist', 'value5', 'value6')

        # lrange(name, start, end)示例
        values = r.lrange('mylist', 0, -1)
        print(values)

        # lindex(name, index)示例
        value = r.lindex('mylist', 2)
        print(value)

        # llen(name)示例
        length = r.llen('mylist')
        print(length)

        # lpop(name)示例
        value = r.lpop('mylist')
        print(value)

        # rpop(name)示例
        value = r.rpop('mylist')
        print(value)

        # lrem(name, num=0, value)示例
        r.lrem('mylist', 0, 'value2')

        # lset(name, index, value)示例
        r.lset('mylist', 1, 'newvalue')

        # ltrim(name, start, end)示例
        r.ltrim('mylist', 0, 2)

        # rpoplpush(src, dst)示例
        r.rpoplpush('mylist', 'mylist2')

        # 打印最终结果
        values = r.lrange('mylist', 0, -1)
        print(values)
        values2 = r.lrange('mylist2', 0, -1)
        print(values2)

        # 删除list 1.redis的delete方法 2.list的ltrim
        # r.delete("mylist")
        # r.ltrim("my_list", 0, -1)
