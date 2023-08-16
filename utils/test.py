# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/11 11:54
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => test.py
"""
from connections import get_redis_pool

redis = get_redis_pool()
message_id = redis.xadd('mystream', {'name': 'Alice', 'age': 30})
print("Added message with ID:", message_id)
