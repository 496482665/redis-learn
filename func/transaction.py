# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/14 17:44
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => transaction.py
"""
from redis import Redis


# =========================== #
#      redis中的事务功能
# =========================== #
class Transaction:
    def start(self, r: Redis):
        try:
            pipeline = r.pipeline()
            # pipeline.multi() # 不需要开启，也能执行事务,开启能更加显式地表示当前处于事务中
        except Exception as e:
            print(e)
            return

        try:
            pipeline.set("t_key_1", "dddxxx")
            pipeline.set("t_key_2", "eee")
            pipeline.set("t_key_3", {"aaa": "bbb"})

            pipeline.execute()
        except Exception as e:
            """
            pipeline.discard()和pipeline.reset()在功能上是相似的，它们都可以用于取消事务并清除命令队列。然而，它们的使用场景可能略有不同。

            主要的区别在于语义上的差异：

            pipeline.discard()方法的名称更加直观，
            它明确表示你要放弃（丢弃）当前事务，并且可以开始一个新的事务。
            它的使用可以更明确地表达你的意图，即取消当前事务并重新开始一个新的事务。

            pipeline.reset()方法的名称则更加通用，它表示重置事务管道并清除命令队列。
            这意味着你可以选择取消当前事务或者清除命令队列以开始一个新的事务。
            它的使用场景可能更灵活，可以用于取消事务，也可以用于开始新的事务。

            总的来说，两者可以互换使用，具体使用哪个方法取决于你对代码的可读性和意图的表达。
            如果你希望更明确地表达你要放弃当前事务并开始新事务的意图，可以使用pipeline.discard()。
            如果你更倾向于一个通用的方法来重置事务管道并清除命令队列，可以使用pipeline.reset()。
            """
            # print(pipeline.discard())
            print(pipeline.reset())

    def start_with_watch(self, r: Redis):
        """
        pipeline.watch是用于监视一个或多个键的变化的方法。
        它可以用来在事务执行之前检测被监视键是否被其他客户端修改，如果有修改，可以选择中断事务的执行。
        """
        # 监视一个键
        r.watch('mykey')

        # 开启事务并返回事务管道对象
        pipe = r.pipeline()
        pipe.multi()

        # 在事务中执行多个命令
        pipe.set('mykey', 'newvalue')
        pipe.get('mykey')

        # 执行事务
        result = pipe.execute()

        # 输出事务执行的结果
        for res in result:
            print(res)
