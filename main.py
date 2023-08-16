# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/7 16:54
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => main.py
"""
from connections import get_redis_pool
from core import String, List, Set, Hash, SortedSet, Stream
from func.transaction import Transaction
from func import pub_sub


# 执行入口
def main():
    redis_instance = get_redis_pool()

    # 基础数据类型
    # String().handle(redis_instance)
    # List().handle(redis_instance)
    # Set().handle(redis_instance)
    # Hash().handle(redis_instance)
    # SortedSet().handle(redis_instance)
    # Stream().handle(redis_instance)

    # 高级功能
    # Transaction().start(redis_instance)
    pub_sub.start(redis_instance)


if __name__ == "__main__":
    main()
