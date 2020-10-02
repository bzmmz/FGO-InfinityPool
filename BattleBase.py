# -*- coding: UTF-8 -*-
from airtest.core.api import *

BATTLE_GAP = 40  # 选完卡后到下一场的等待时间


class BattleBase(object):
    """
    战斗基类
    """

    def __init__(self):
        self.gap = BATTLE_GAP
        self.param = None

        self.skill_gap = 5.0
        self.select_gap = 1.5

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

    def releaseNonTargetClothSkill(self):
        touch(self.param.CLOTH_SKILL)
