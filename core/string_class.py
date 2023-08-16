# -*- coding: utf-8 -*-

"""
  @authoself.inst: tangliqi
  @date: 2023/8/7 17:17
  @python veself.instsion: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => string_class.py
"""
from redis import Redis

from core.base import BaseDataType


# =========================== #
#      操作redis的string功能
# =========================== #
# Redis Strings存储字节序列，包括文本、序列化对象和二进制数组。
# 因此，字符串是最基本的 Redis 数据类型。
# 通常用于缓存，也可以实现计数器并执行按位操作。
class String(BaseDataType):
    """
    set(name, value, ex=None, px=None, nx=False, xx=False): 设置指定键的值。
    get(name): 获取指定键的值。
    mset(mapping): 批量设置多个键值对。
    mget(keys, *args): 批量获取多个键的值。
    append(key, value): 在指定键的值后追加字符串。
    strlen(key): 获取指定键的值的字符串长度。
    incr(name, amount=1): 将指定键的值增加指定的整数值。
    decr(name, amount=1): 将指定键的值减少指定的整数值。
    incrby(name, amount): 将指定键的值增加指定的整数值。
    decrby(name, amount): 将指定键的值减少指定的整数值。
    getrange(key, start, end): 获取指定键的值的子字符串。
    setrange(key, offset, value): 在指定键的值中，从指定偏移位置开始，替换为指定字符串。
    getset(key, value): 设置指定键的值，并返回原来的值。
    setex(name, time, value): 设置指定键的值，并指定过期时间（以秒为单位）。
    psetex(name, time_ms, value): 设置指定键的值，并指定过期时间（以毫秒为单位）。
    setnx(name, value): 当指定键不存在时，设置键的值。
    getbit(name, offset): 获取指定键的值的位值。
    setbit(name, offset, value): 设置指定键的值的位值。
    bitcount(name, start=None, end=None): 统计指定键的值中，指定范围内的位为1的个数。
    bitop(operation, dest, *keys): 对多个键的值执行位操作，并将结果保存在目标键中。
    bitpos(name, bit, start=None, end=None): 获取指定键的值中，指定位值第一次出现的位置。
    """

    def handle(self, r: Redis):
        # set(name, value)示例
        r.set('mykey', 'Hello Redis')

        # get(name)示例
        value = r.get('mykey')
        print(value)

        # mset(mapping)示例
        r.mset({'key1': 'value1', 'key2': 'value2'})

        # mget(keys, *args)示例
        values = r.mget(['key1', 'key2'])
        print(values)

        # append(key, value)示例
        r.append('mykey', ' World')
        value = r.get('mykey')
        print(value)

        # strlen(key)示例
        length = r.strlen('mykey')
        print(length)

        # incr(name, amount=1)示例
        r.set('count', 10)
        r.incr('count')
        count = r.get('count')
        print(count)

        # decr(name, amount=1)示例
        r.decr('count')
        count = r.get('count')
        print(count)

        # incrby(name, amount)示例
        r.incrby('count', 5)
        count = r.get('count')
        print(count)

        # decrby(name, amount)示例
        r.decrby('count', 3)
        count = r.get('count')
        print(count)

        # getrange(key, start, end)示例
        substring = r.getrange('mykey', 0, 4)
        print(substring)

        # setrange(key, offset, value)示例
        r.setrange('mykey', 6, 'Mysql')
        value = r.get('mykey')
        print(value)

        # getset(key, value)示例
        old_value = r.getset('mykey', 'New Value')
        print(old_value)

        # setex(name, time, value)示例
        r.setex('mykey', 10, 'Value with expiration')
        value = r.get('mykey')
        print(value)

        # setnx(name, value)示例
        r.setnx('mykey', 'New Value')
        value = r.get('mykey')
        print(value)

        # getbit(name, offset)示例
        bit = r.getbit('mykey', 2)
        print(bit)

        # setbit(name, offset, value)示例
        r.setbit('mykey', 5, 1)
        bit = r.getbit('mykey', 5)
        print(bit)

        # bitcount(name, start=None, end=None)示例
        count = r.bitcount('mykey')
        print(count)

        # bitop(operation, dest, *keys)示例
        r.set('key1', '101010')
        r.set('key2', '111000')
        r.bitop('AND', 'result', 'key1', 'key2')
        result = r.get('result')
        print(result)

        # bitpos(name, bit, start=None, end=None)示例
        position = r.bitpos('mykey', 1)
        print(position)
