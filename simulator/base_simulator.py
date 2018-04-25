# -*- coding:utf-8 _*-
""" 
@author:mlliu
@file: base_simulator.py 
@time: 2018/04/25 
"""


class BaseSimulator(object):
    """
    用户模拟器基类, 定义方法类型
    """

    def __init__(self):
        super(BaseSimulator, self).__init__()

    def init_episode(self):
        """
        TODO: 清空模拟器状态，重新装入一段新的对话
        :return:
        """
        pass

    def next(self):
        """
        TODO: 用户模拟器下一个动作，输出下一段需要输出的文本
        :return: 下一个输出文本
        """
        pass

    def set_nlg_model(self, nlg_model):
        self.nlg = nlg_model

    def set_slu_model(self, slu_model):
        self.slu = slu_model

