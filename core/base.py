# -*- coding: utf-8 -*-

"""
  @author: tangliqi
  @date: 2023/8/8 10:15
  @python version: 3.6 
  @contact me: 110
  ---------------------------------------
  @desc: redis-learn => base.py
"""
from abc import abstractmethod


class BaseDataType:
    @abstractmethod
    def handle(self, *args, **kwargs):
        raise NotImplemented()
