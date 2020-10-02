# -*- encoding=utf8 -*-
from airtest.core.api import *


class UninializedException(Exception):
    pass


class UnFoundException(Exception):
    pass


class Choose(object):
    """
        负责选助战,直至进战
    """

    def __init__(self):
        self.targets = []
        self.found = None
        # 刷新CD
        self.refresh_cool_down = 10
        self.refresh_button_pos = None
        self.confirm_button_pos = None
        self.start_button_pos = None
        # 点击按钮的反应和转场
        self.short_gap = 3.0
        self.long_gap = 5.0
        self.battle_gap = 40.0

    def setRefreshButtonPos_XY(self, x, y):
        self.refresh_button_pos = [x, y]

    def setRefreshButtonPos(self, pos):
        self.refresh_button_pos = pos

    def setConfirmButtonPos_XY(self, x, y):
        self.confirm_button_pos = [x, y]

    def setConfirmButtonPos(self, pos):
        self.confirm_button_pos = pos

    def setStartButtonPos_XY(self, x, y):
        self.start_button_pos = [x, y]

    def setStartButtonPos(self, pos):
        self.start_button_pos = pos

    def appendTarget(self, target):
        """
        Args:
            target: 目标，截带礼装头像

        Returns:

        """
        self.targets.append(target)

    def findTarget(self):
        """
        寻找目标
        Returns:

        """
        if len(self.targets) <= 0:
            raise UninializedException()

        while True:
            for p in self.targets:
                if exists(p):
                    self.found = p
                    break

            if self.found is None:
                self.refresh()
                continue
            else:
                break

    def refresh(self):
        """
        刷新助战
        Returns:

        """
        touch(self.refresh_button_pos)
        sleep(self.short_gap)
        touch(self.confirm_button_pos)

    def selectChoose(self):
        if self.found is None:
            raise UnFoundException()
        touch(self.found)
        sleep(self.long_gap)
        touch(self.start_button_pos)
        sleep(self.battle_gap)

    def process(self):
        self.findTarget()
        self.selectChoose()
