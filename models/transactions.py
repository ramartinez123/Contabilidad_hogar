class Transactions:
    def __init__(self,id_AccountingTransactions,FkidVAccount, FkidSubAccount, FkidVIncreasedBY,
                 accruedDate,amount,FKidCountry,FkidCity,comment,FkidDues):
        self.id_AccountingTransactions = id_AccountingTransactions
        self.FkidVAccount = FkidVAccount
        self.FkidSubAccount = FkidSubAccount
        self.FkidVIncreasedBY = FkidVIncreasedBY
        self.accruedDate = accruedDate
        self.amount = amount
        self.FKidCountry = FKidCountry
        self.FkidCity = FkidCity
        self.comment = comment
        self.FkidDues = FkidDues

    def getid_AccountingTransactions(self):
        return self.id_AccountingTransactions

    def setid_AccountingTransactions(self,x):
        self.id_AccountingTransactions =x

    def getFkidVAccount(self):
        return self.FkidVAccount

    def setFkidVAccount(self,FkidVAccount):
        self.FkidVAccount =FkidVAccount

    def getFkidSubAccount(self):
        return self.FkidSubAccount

    def setFkidSubAccount(self,x):
        self.FkidSubAccount =x

    def getFkidVIncreasedBY(self):
        return self.FkidVIncreasedBY

    def setFkidVIncreasedBY(self,x):
        self.FkidVIncreasedBY =x

    def getaccruedDate(self):
        return self.accruedDate

    def setaccruedDate(self,x):
        self.accruedDate =x

    def getamount(self):
        return self.amount

    def setamount(self,x):
        self.amount, =x

    def getFKidCountry(self):
        return self.FKidCountry

    def setFKidCountry(self,x):
        self.FKidCountry =x

    def getFkidCity(self):
        return self.FkidCity

    def setFkidCity(self,x):
        self.FkidCity =x

    def getcomment(self):
        return self.comment

    def setcomment(self,x):
        self.comment =x

    def getFkidDues(self):
        return self.FkidDues

    def setFkidDues(self,x):
        self.FkidDues =x

