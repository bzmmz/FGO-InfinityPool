# -*- coding: utf8  -*-
# 1920*1080模拟器分辨率参数
from ParamBase import paramBase


class param_1080P(paramBase):
    def __init__(self):
        super(param_1080P, self).__init__()
        self.REFRESH_BUTTON_POS = [1275, 180]
        self.CONFIRM_BUTTON_POS = [1250, 830]
        self.CARD_1 = [200, 755]
        self.CARD_2 = [555, 755]
        self.CARD_3 = [960, 755]
        self.CARD_4 = [1350, 755]
        self.CARD_5 = [1720, 755]
        self.BAOJU_1 = [600, 300]
        self.BAOJU_2 = [960, 300]
        self.BAOJU_3 = [1300, 300]
        # CxSx->character x skill x
        self.C1_S1 = [100, 845]
        self.C1_S2 = [235, 845]
        self.C1_S3 = [400, 845]
        self.C2_S1 = [580, 845]
        self.C2_S2 = [710, 845]
        self.C2_S3 = [860, 845]
        self.C3_S1 = [1055, 845]
        self.C3_S2 = [1195, 845]
        self.C3_S3 = [1330, 845]
        # 衣服技能
        self.CLOTH_SKILL = [1780, 460]
        self.CLOTH_SKILL_1 = [1350, 455]
        self.CLOTH_SKILL_2 = [1480, 455]
        self.CLOTH_SKILL_3 = [1600, 455]
        # 指向性技能目标
        self.SKILL_TARGET_1 = [500, 660]
        self.SKILL_TARGET_2 = [955, 660]
        self.SKILL_TARGET_3 = [1410, 660]
        # 选卡命令
        self.ATTACK_BUTTON = [1660, 900]
        # 结束相关
        self.END_CLICK_POS = [900, 860]
        self.END_CONFIRM_POS = [1620, 980]
        self.NEXT_GAME = [1250, 830]

_param_1080P = param_1080P()
