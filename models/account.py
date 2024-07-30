class Account:
    def __init__(self,idAccount,Account,FkidVAccountType, FkidAccountingItem, FkidVIncreasedBY,
                 FkidAccountingMethod,FKidCurrency,Detalle):
        self.idAccount = idAccount
        self.Account = Account
        self.FkidVAccountType = FkidVAccountType
        self.FkidAccountingItem = FkidAccountingItem
        self.FkidVIncreasedBY = FkidVIncreasedBY
        self.FkidAccountingMethod = FkidAccountingMethod
        self.FKidCurrency = FKidCurrency
        self.Detalle = Detalle
       
    def getidAccount(self):
        return self.idAccount

    def setidAccount(self,value):
        self.idAccount =value

    def getAccount(self):
        return self.Account

    def setAccount(self,value):
        self.Account =value

    def getFkidVAccountType(self):
        return self.FkidVAccountType

    def setFkidVAccountType(self,value):
        self.FkidVAccountType =value

    def getFkidAccountingItem(self):
        return self.FkidAccountingItem

    def setFkidAccountingItem(self,value):
        self.FkidAccountingItem =value

    def getFkidVIncreasedBY(self):
        return self.FkidVIncreasedBY

    def setFkidVIncreasedBY(self,value):
        self.FkidVIncreasedBY =value

    def getFkidAccountingMethod(self):
        return self.FkidAccountingMethod

    def setFkidAccountingMethod(self,value):
        self.FkidAccountingMethod =value 
    
    def getFKidCurrency(self):
        return self.FKidCurrency

    def setFKidCurrency(self,value):
        self.FKidCurrency =value 

    def getDetalle(self):
        return self.Detalle

    def setDetalle(self,value):
        self.Detalle =value 
