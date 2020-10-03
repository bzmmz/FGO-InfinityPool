# -*- coding: UTF-8 -*-
# 大英雄一面 + WCBA + np礼服 2，3面
# 大英雄1号位绿卡打手2号位
from BattleBase import BattleBase
from airtest.core.api import *


class WCBA_Arash(BattleBase):

    def __init__(self, param, end_signal):
        super(WCBA_Arash, self).__init__(param)
        self.end_signal = end_signal

    def process(self):
        self.battle_1()
        self.battle_2()
        self.battle_3()

        self.moreBattle()

    def battle_1(self):
        self.releaseNonTargetSkill(self.param.C1_S3)
        touch(self.param.ATTACK_BUTTON)
        sleep(self.select_gap)
        touch(self.param.BAOJU_1)
        self.normalAttack()

    def battle_2(self):
        self.releaseTargetClothSkill(self.param.CLOTH_SKILL_2, self.param.SKILL_TARGET_2)
        self.releaseTargetSkill(self.param.C1_S1, self.param.SKILL_TARGET_2)
        self.releaseTargetSkill(self.param.C3_S1, self.param.SKILL_TARGET_2)
        self.releaseNonTargetSkill(self.param.C2_S2)

        touch(self.param.ATTACK_BUTTON)
        sleep(self.select_gap)
        touch(self.param.BAOJU_2)
        self.normalAttack()

    def battle_3(self):
        self.releaseNonTargetSkill(self.param.C1_S2)
        self.releaseNonTargetSkill(self.param.C3_S2)
        self.releaseNonTargetSkill(self.param.C2_S1)
        self.releaseTargetSkill(self.param.C1_S3, self.param.SKILL_TARGET_2)

        touch(self.param.ATTACK_BUTTON)
        sleep(self.select_gap)
        touch(self.param.BAOJU_2)
        self.normalAttack()

    def moreBattle(self):
        while True:
            if not exists(self.end_signal):
                self.normalAttack()
            else:
                break

    def normalAttack(self):
        sleep(self.card_gap)
        touch(self.param.CARD_1)
        sleep(self.card_gap)
        touch(self.param.CARD_2)
        sleep(self.card_gap)
        touch(self.param.CARD_3)
        sleep(self.card_gap)
        sleep(self.gap)
