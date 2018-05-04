# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from CARD_INFO import TCardInfo
from CARD_INFO import TCardList

class Avatar(KBEngine.Proxy):
    def __init__(self):
        self.NameB = self.CellData["NameA"]
        self.bf = self.CellData["Battlefield"]
        self.createCellEntity(self.bf )

