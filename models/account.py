class Account:
    def __init__(self,idAccount,Account,FkidVAccountType, FkidAccountingItem, FkidVIncreasedBY,
                 FkidAccountingMethod,FKidCourrency,Detalle):
        self.idAccount = idAccount
        self.Account = Account
        self.FkidVAccountType = FkidVAccountType
        self.FkidAccountingItem = FkidAccountingItem
        self.FkidVIncreasedBY = FkidVIncreasedBY
        self.FkidAccountingMethod = FkidAccountingMethod
        self.FKidCourrency = FKidCourrency
        self.Detalle = Detalle
       
    def getidAccount(self):
        return self.idAccount

    def setidAccount(self,x):
        self.idAccount =x

    def getAccount(self):
        return self.Account

    def setAccount(self,x):
        self.Account =x

    def getFkidVAccountType(self):
        return self.FkidVAccountType

    def setFkidVAccountType(self,x):
        self.FkidVAccountType =x

    def getFkidAccountingItem(self):
        return self.FkidAccountingItem

    def setFkidAccountingItem(self,x):
        self.FkidAccountingItem =x

    def getFkidVIncreasedBY(self):
        return self.FkidVIncreasedBY

    def setFkidVIncreasedBY(self,x):
        self.FkidVIncreasedBY =x

    def getFkidAccountingMethod(self):
        return self.FkidAccountingMethod

    def setFkidAccountingMethod(self,x):
        self.FkidAccountingMethod =x  
    
    def getFKidCourrency(self):
        return self.FKidCourrency

    def setFKidCourrency(self,x):
        self.FKidCourrency =x 

    def getDetalle(self):
        return self.Detalle

    def setDetalle(self,x):
        self.Detalle =x 
