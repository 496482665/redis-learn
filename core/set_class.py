# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/8 10:14
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => set_class.py
"""
from redis import Redis

from core.base import BaseDataType


# =========================== #
#      操作redis的set功能
# =========================== #
# Redis的Set底层数据结构是一个由哈希表和布隆过滤器组成的数据结构。
# 它提供了高效的插入、删除和查找操作，同时保证了集合中元素的唯一性。
class Set(BaseDataType):
    """
    sadd(key, *values)：向集合中添加一个或多个元素。
    srem(key, *values)：从集合中移除一个或多个元素。
    sismember(key, value)：检查给定元素是否是集合的成员。
    scard(key)：获取集合的成员数量。
    smembers(key)：获取集合的所有成员。
    srandmember(key, count=None)：从集合中随机获取一个或多个元素。
    spop(key)：随机弹出并返回集合中的一个元素。
    smove(src, dest, value)：将元素从源集合移动到目标集合。
    sinter(keys, *args)：计算多个集合的交集。
    sunion(keys, *args)：计算多个集合的并集。
    sdiff(keys, *args)：计算多个集合的差集。
    sinterstore(dest, keys, *args)：计算多个集合的交集，并将结果存储到目标集合。
    sunionstore(dest, keys, *args)：计算多个集合的并集，并将结果存储到目标集合。
    sdiffstore(dest, keys, *args)：计算多个集合的差集，并将结果存储到目标集合。
    """

    def handle(self, client: Redis):
        # sadd(key, *values): 向集合添加一个或多个元素
        client.sadd('myset', 'apple', 'banana', 'cherry')

        # srem(key, *values): 从集合中移除一个或多个元素
        client.srem('myset', 'banana')

        # sismember(key, value): 检查元素是否是集合的成员
        is_member = client.sismember('myset', 'apple')
        is_member1 = client.sismember('mtset', 'banana')
        print("Is 'apple' a member of the set:", is_member)
        print("Is 'banana' a member of the set:", is_member1)

        # scard(key): 获取集合的成员数量
        num_members = client.scard('myset')
        print("Number of members in the set:", num_members)

        # smembers(key): 获取集合的所有成员
        members = client.smembers('myset')
        print("Members of the set:", members)

        # srandmember(key, count=None): 从集合中随机获取一个或多个元素
        random_members = client.srandmember('myset', 2)
        print("Random members from the set:", random_members)

        # smove(src, dest, value): 将元素从源集合移动到目标集合
        client.sadd('another_set', 'date')
        client.smove('myset', 'another_set', 'cherry')

        # spop(key): 随机弹出并返回集合中的一个元素
        popped_member = client.spop('myset')
        print("Popped member:", popped_member)

        client.sadd('set1', 'apple', 'banana', 'cherry')
        client.sadd('set2', 'banana', 'cherry', 'date')

        # sinter(keys, *args): 计算多个集合的交集
        intersection_result = client.sinter('set1', 'set2')
        print("Intersection of sets:", intersection_result)

        # sunion(keys, *args): 计算多个集合的并集
        union_result = client.sunion('set1', 'set2')
        print("Union of sets:", union_result)

        # sdiff(keys, *args): 计算多个集合的差集
        diff_result = client.sdiff('set1', 'set2')
        print("Difference of sets:", diff_result)

        # sinterstore(dest, keys, *args): 计算多个集合的交集，并将结果存储到目标集合
        client.sinterstore('intersection_set', 'set1', 'set2')

        # sunionstore(dest, keys, *args): 计算多个集合的并集，并将结果存储到目标集合
        client.sunionstore('union_set', 'set1', 'set2')

        # sdiffstore(dest, keys, *args): 计算多个集合的差集，并将结果存储到目标集合
        client.sdiffstore('diff_set', 'set1', 'set2')

        # 删除set
        client.delete("another_set")
