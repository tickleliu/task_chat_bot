# -*- coding:utf-8 -*-
""" 
@author:mlliu
@file: rule_simulator.py 
@time: 2018/04/25 
"""

import dialog_config
from .base_simulator import BaseSimulator


class RuleSimulator(BaseSimulator):
    """

    """

    def __init__(self, act_set=None, max_turn=None):
        """

        """
        self.act_set = act_set
        self.max_turn = max_turn
        super(RuleSimulator, self).__init__()
        pass

    def __del__(self):
        pass

    def seq_to_attr(self, seq):
        """
        TODO: 把输入的口语句子seq转为attr列表
        :param seq:
        :return:
        """
        pass

    def init_episode(self, goal, zhusu_list, hpi_list):
        """
        重新开起一段对话
        :param goal: 患者实际需要就诊的门诊科室
        :param zhusu_list: 患者主诉
        :param hpi_list: 患者现病史
        :return:
        """

        self.stat = {}
        self.stat["goal"] = goal
        self.stat["zhusu"] = zhusu_list
        self.stat["hpi"] = hpi_list
        self.stat["turn"] = 0  # 当前对话轮数
        self.stat["un_request_attr"] = []  # 未获得询问的患者状态
        self.stat["request_attr"] = []  # 已经被询问过得患者状态
        self.dialog_status = dialog_config.NO_OUTCOME_YET

    def next(self, system_action):
        self.stat["turn"] += 1

        if self.max_turn is not None and self.stat["turn"] > self.max_turn:
            self.episode_over = True
            self.stat["diaact"] = "closing"
            self.dialog_status = dialog_config.FAILED_DIALOG
        else:
            pass

    def response_confirm(self):
        pass

    def response_deny(self):
        pass

    def response_thanks(self):
        pass

    def start(self):
        pass
