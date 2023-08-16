# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/8 11:45
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => hash_class.py
"""
from redis import Redis

from core.base import BaseDataType


# =========================== #
#      操作redis的hash功能
# =========================== #
# Redis中的Hash是一种键值对存储的数据结构，类似于Python中的字典。
# Hash结构可以将多个字段（field）与对应的值（value）关联起来，并且可以将多个Hash结构存储在一个键中。
# Hash结构在存储和获取数据时具有高效的性能，适用于存储和操作复杂的数据对象。
class Hash(BaseDataType):
    """
    hdel(name, *keys): 删除一个或多个字段。
    hexists(name, key): 判断字段是否存在。
    hget(name, key): 获取指定字段的值。
    hgetall(name): 获取Hash中所有字段和值。
    hincrby(name, key, amount=1): 将指定字段的值增加给定的增量。
    hincrbyfloat(name, key, amount=1.0): 将指定字段的值增加给定的浮点增量。
    hkeys(name): 获取Hash中所有字段。
    hlen(name): 获取Hash中字段的数量。
    hmget(name, keys, *args): 获取多个字段的值。
    hmset(name, mapping): 批量设置多个字段的值。
    hset(name, key, value): 设置字段的值。
    hsetnx(name, key, value): 设置字段的值，只有当字段不存在时才设置。
    hvals(name): 获取Hash中所有值。
    """

    def handle(self, redis_client: Redis):
        # hset(name, key, value): 设置Hash中指定字段的值
        # 或者通过dict传入多个值，hmset不再使用了
        # hmset(name, mapping): 批量设置Hash中的多个字段值
        # client.hmset('user:1', {'age': 25, 'gender': 'female'}) x
        redis_client.hset('myhash', 'name', 'Alice', {'age': 25, 'gender': 'female', "field2": "hhh"})

        # hdel(name, *keys) - 删除一个或多个字段
        redis_client.hdel("myhash", "field1", "field2")
        print(redis_client.hgetall("myhash"))

        # hexists(name, key) - 判断字段是否存在
        result = redis_client.hexists("myhash", "field1")
        print(result)

        # hget(name, key) - 获取指定字段的值
        value = redis_client.hget("myhash", "age")
        print(value)

        # hgetall(name) - 获取Hash中所有字段和值
        result = redis_client.hgetall("myhash")
        print(result)

        # hincrby(name, key, amount=1) - 将指定字段的值增加给定的增量,可以为负数
        new_value = redis_client.hincrby("myhash", "age", 5)
        print(new_value)

        # hincrbyfloat(name, key, amount=1.0) - 将指定字段的值增加给定的浮点增量,可以为负数
        new_value = redis_client.hincrbyfloat("myhash", "age", -2.5)
        print(new_value)

        # hkeys(name) - 获取Hash中所有字段
        keys = redis_client.hkeys("myhash")
        print(keys)

        # hlen(name) - 获取Hash中字段的数量
        length = redis_client.hlen("myhash")
        print(length)

        # hmget(name, keys, *args) - 获取多个字段的值
        values = redis_client.hmget("myhash", ["age", "name"])
        print(values)

        # hsetnx(name, key, value) - 设置字段的值，只有当字段不存在时才设置
        success = redis_client.hsetnx("myhash", "field1", "value1")
        print(success)

        # hvals(name) - 获取Hash中所有值
        values = redis_client.hvals("myhash")
        print(values)

        # 删除hash
        redis_client.delete("myhash")