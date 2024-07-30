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

    def setid_AccountingTransactions(self,value):
        self.id_AccountingTransactions =value

    def getFkidVAccount(self):
        return self.FkidVAccount

    def setFkidVAccount(self,FkidVAccount):
        self.FkidVAccount =FkidVAccount

    def getFkidSubAccount(self):
        return self.FkidSubAccount

    def setFkidSubAccount(self,value):
        self.FkidSubAccount =value

    def getFkidVIncreasedBY(self):
        return self.FkidVIncreasedBY

    def setFkidVIncreasedBY(self,value):
        self.FkidVIncreasedBY =value

    def getaccruedDate(self):
        return self.accruedDate

    def setaccruedDate(self,value):
        self.accruedDate =value

    def getamount(self):
        return self.amount

    def setamount(self,value):
        self.amount =value

    def getFKidCountry(self):
        return self.FKidCountry

    def setFKidCountry(self,value):
        self.FKidCountry =value

    def getFkidCity(self):
        return self.FkidCity

    def setFkidCity(self,value):
        self.FkidCity =value

    def getcomment(self):
        return self.comment

    def setcomment(self,value):
        self.comment =value

    def getFkidDues(self):
        return self.FkidDues

    def setFkidDues(self,value):
        self.FkidDues =value

