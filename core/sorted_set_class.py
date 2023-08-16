# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/8 15:12
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => sorted_set_class.py
"""
from redis import Redis

from core.base import BaseDataType


# =========================== #
#      操作redis的sorted set功能
# =========================== #
# 在Redis中，Sorted Set（有序集合）是一种有序的集合，其中的每个元素都关联着一个分数（score），分数用于对元素进行排序。
# Sorted Set内部使用了两种数据结构：跳跃表（Skip List）和哈希表（Hash Table），使得插入、删除、查找等操作的时间复杂度都能保持在O(log N)级别
class SortedSet(BaseDataType):
    """
    zadd(name, mapping) - 向Sorted Set中添加一个或多个成员
    zcard(name) - 获取Sorted Set中成员的数量
    zcount(name, min, max) - 获取分数在指定范围内的成员数量
    zincrby(name, amount, value) - 为Sorted Set中的某个成员增加分数
    zinterstore(dest, keys, aggregate=None) - 计算多个Sorted Set的交集，并将结果存储到一个新的Sorted Set中
    zlexcount(name, min, max) - 获取成员在字典序范围内的数量
    zrange(name, start, end, withscores=False, score_cast_func=float) - 获取指定范围内的成员
    zrangebylex(name, min, max, start=None, num=None) - 获取字典序范围内的成员
    zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float) - 获取分数范围内的成员
    zrank(name, value) - 获取成员在Sorted Set中的排名（从小到大）
    zrem(name, *values) - 从Sorted Set中移除一个或多个成员
    zremrangebylex(name, min, max) - 移除字典序范围内的成员
    zremrangebyrank(name, start, end) - 移除排名范围内的成员
    zremrangebyscore(name, min, max) - 移除分数范围内的成员
    zrevrange(name, start, end, withscores=False, score_cast_func=float) - 获取指定范围内的成员（从大到小）
    zrevrangebylex(name, max, min, start=None, num=None) - 获取字典序范围内的成员（从大到小）
    zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float) - 获取分数范围内的成员（从大到小）
    zrevrank(name, value) - 获取成员在Sorted Set中的排名（从大到小）
    zscore(name, value) - 获取成员的分数
    zunionstore(dest, keys, aggregate=None) - 计算多个Sorted Set的并集，并将结果存储到一个新的Sorted Set中
    zscan(name, cursor=0, match=None, count=None, score_cast_func=float) - 迭代遍历Sorted Set的成员
    """

    def handle(self, client: Redis):
        # zadd(name, mapping, nx=False, xx=False, ch=False, incr=False): 向有序集合添加一个或多个成员
        client.zadd('leaderboard', {'Alice': 100, 'Bob': 200, 'Charlie': 150})

        # zscore(name, value): 获取有序集合中成员的分数
        score = client.zscore('leaderboard', 'Bob')
        print("Score of Bob:", score)

        # zrank(name, value, reverse=False): 获取有序集合中成员的排名（从小到大）
        rank = client.zrank('leaderboard', 'Bob')
        print("Rank of Bob:", rank)

        # zrevrank(name, value): 获取有序集合中成员的排名（从大到小）
        rev_rank = client.zrevrank('leaderboard', 'Bob')
        print("Reverse rank of Bob:", rev_rank)

        # zrange(name, start, end, withscores=False, score_cast_func=<class 'float'>): 获取有序集合中指定排名范围的成员
        members = client.zrange('leaderboard', 0, -1, withscores=True)
        print("Members and scores:", members)

        # zrevrange(name, start, end, withscores=False, score_cast_func=<class 'float'>): 获取有序集合中指定排名范围的成员（从大到小）
        rev_members = client.zrevrange('leaderboard', 0, -1, withscores=True)
        print("Reverse members and scores:", rev_members)

        # zrem(name, *values): 移除有序集合中一个或多个成员
        value = client.zrem('leaderboard', 'Charlie')
        print("zrem value:", value)

        # zincrby(name, amount, value): 有序集合中成员的分数增加
        client.zincrby('leaderboard', 50, 'Bob')
        print(client.zscore('leaderboard', "Bob"))

        # zcount(name, min, max): 获取有序集合中分数范围内的成员数量
        count = client.zcount('leaderboard', 100, 200)
        print("Number of members in score range:", count)

        # zcard(name): 获取有序集合的成员数量
        num_members = client.zcard('leaderboard')
        print("Number of members:", num_members)

        # zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=<class 'float'>):
        # 根据分数范围获取有序集合的成员
        members_by_score = client.zrangebyscore('leaderboard', 100, 200, withscores=True)
        print("Members in score range:", members_by_score)

        # zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=<class 'float'>):
        # 根据分数范围获取有序集合的成员（从大到小）
        rev_members_by_score = client.zrevrangebyscore('leaderboard', 200, 100, withscores=True)
        print("Reverse members in score range:", rev_members_by_score)

        # zremrangebyrank(name, start, end): 移除有序集合中排名范围内的成员
        client.zremrangebyrank('leaderboard', 0, 1)

        # zremrangebyscore(name, min, max): 移除有序集合中分数范围内的成员
        client.zremrangebyscore('leaderboard', 100, 150)

        # zinterstore(dest, keys, aggregate=None): 计算多个有序集合的交集，并将结果存储到目标有序集合
        client.zadd('sorted_set1', {'a': 1, 'b': 2, 'c': 3})
        client.zadd('sorted_set2', {'b': 3, 'c': 4, 'd': 5})
        client.zinterstore('intersection', {'sorted_set1': 1, 'sorted_set2': 1}, aggregate='MIN')

        # zunionstore(dest, keys, aggregate=None): 计算多个有序集合的并集，并将结果存储到目标有序集合
        client.zunionstore('union_sorted_set', {'sorted_set1': 1, 'sorted_set2': 1}, aggregate='MAX')