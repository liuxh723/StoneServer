# -*- coding: utf-8 -*-
import KBEngine
import d_card_dis
import random
import re
from KBEDebug import *
from array import *


class Battlefield(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        DEBUG_MSG('BattleField.cell::__init__')