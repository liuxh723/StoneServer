# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import random

class Account(KBEngine.Proxy):
	def __init__(self):
		self.Gold = 999999
		#self.randomInitKZ()
		KBEngine.Proxy.__init__(self)

	def randomInitKZ(self):
		ls = []
		for i in range(30):
			ls.append(random.randint(10000001, 10000050))
		roleType = 0
		name = "随机生成卡组"
		index = -1
		self.reqEditCardGroup(roleType, ls, name, index)

	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
		
	def onClientEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT

	def reqChangeName(self, name):
		"""
        更改name
        :param self:
        :param name:
        :return:
        """
		DEBUG_MSG("Account[%i].reqChangeName:%s" % (self.id, name))
		if name == "":
			return
		self.Name = name

	def reqChangeLevel(self, lv):
		INFO_MSG("account[%i] level:%s" % lv)

	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()

	def reqBuyKabao(self,buyNum):
		DEBUG_MSG("Account[%i].reqBuyKabao:%s" % (self.id, buyNum))
		if self.Gold <= buyNum*100:
			return
		self.Gold -= buyNum*100
		self.Kabao += buyNum
		DEBUG_MSG("Account[%i].Gold:%s" % (self.id, self.Gold))
		DEBUG_MSG("Account[%i].Kabao:%s" % (self.id, self.Kabao))

	def reqOpenKabao(self):
		DEBUG_MSG("Account[%i].reqOpenKabao" % self.id)
		if self.Kabao <1:
			return
		self.Kabao -= 1
		DEBUG_MSG("Account[%i].Kabao:%s" % (self.id, self.Kabao))
		ls = []
		for i in range(5):
			f = random.randint(10000001,10000051)
			ls.append(f)
			self.AddCard(f)
		self.client.onOpenPack(ls)
		self.CardList = self.CardList

	def AddCard(self, cardID):
		for i in range(len(self.CardList)):
			if self.CardList[i]["CardID"] == cardID:
				self.CardList[i]["CardNum"] += 1
				return
		dic = {"CardID": cardID, "CardNum": 1, }
		self.CardList.append(dic)
		DEBUG_MSG("Account[%i].CardList:%s" % (self.id, len(self.CardList)))



	def reqEditCardGroup(self,CardGroupInfo):
		DEBUG_MSG("Account[%i].reqEditCardGroup" % (self.id,))
		self.CardGroupList = CardGroupInfo
		

	def reqDelCardGroup(self,index):
		DEBUG_MSG("Account[%i].reqDelCardGroup:%s" % (self.id, index))
		if index > len(self.CardGroupList)-1:
			return
		del self.CardGroupList[index]

	def reqCardList(self):
		DEBUG_MSG("Account[%i].reqCardList!" % (self.id))
		self.client.onReqCardList(self.CardList,self.CardGroupList)





