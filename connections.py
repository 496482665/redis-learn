# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/7 16:55
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => connections.py
"""
import redis


# 获取单个redis实例
def get_redis_connect(host="localhost", port=6379, decode=True):
    """
    获取单个redis实例

    :param host:
    :param port:
    :param decode:
    :return:
    """
    return redis.Redis(host=host, port=port, decode_responses=decode)


# =========================== #
#  使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
#  可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池
# =========================== #
def get_redis_pool(host="localhost", port=6379, db=0, decode=True):
    """
    获取redis连接池

    :param host:
    :param port:
    :param db:
    :param decode:
    :return:
    """
    connection_pool = redis.ConnectionPool(host=host, port=port, db=db)

    return redis.Redis(connection_pool=connection_pool, decode_responses=decode)
