# -*- coding: UTF-8 -*-
from airtest.core.api import *
from ParamBase import paramBase
import BattleBaseParam as bp

class BattleBase(object):
    """
    战斗基类,处理加载完之后进入战斗界面三面战斗
    """

    def __init__(self, param):
        """

        Args:
            param (paramBase):参数
        """
        self.gap = bp.BATTLE_GAP
        self.param = param

        self.skill_gap = bp.SKILL_GAP
        self.select_gap = bp.SELCET_GAP
        self.card_gap = bp.CARD_GAP

    # 释放不取对象技能
    def releaseNonTargetSkill(self, skill_pos):
        """

        Args:
            skill_pos ([x, y]):技能图标所在的位置

        Returns:

        """
        touch(skill_pos)
        sleep(self.skill_gap)

    # 释放取对象技能
    def releaseTargetSkill(self, skill_pos, target_pos):
        """

        Args:
            skill_pos ([x, y]):技能图标所在位置
            target_pos ([x, y]): 目标位置

        Returns:

        """
        touch(skill_pos)
        sleep(self.select_gap)
        touch(target_pos)
        sleep(self.skill_gap)

    # 御主礼服技能
    def releaseNonTargetClothSkill(self, skill_pos):
        touch(self.param.CLOTH_SKILL)
        sleep(self.select_gap)
        self.releaseNonTargetSkill(skill_pos)

    def releaseTargetClothSkill(self, skill_pos, target_pos):
        touch(self.param.CLOTH_SKILL)
        sleep(self.select_gap)
        self.releaseTargetSkill(skill_pos, target_pos)

    def setParam(self, param):
        """

        Args:
            param (paramBase):

        Returns:

        """
        self.param = param

    def process(self):
        pass
