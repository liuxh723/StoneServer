# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
#from interfaces.cardBase import cardBase
import d_card_dis


class Avatar(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        DEBUG_MSG('Avatar.cell::__init__: [%i]  roleType:[%i]' % (self.id, self.roleType))
