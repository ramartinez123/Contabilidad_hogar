class Exchange:
    def __init__(self,id_Exchange,dateCoti, FkidCurrency, importeCot):
                 
        self.id_Exchange = id_Exchange
        self.dateCoti = dateCoti
        self.FkidCurrency = FkidCurrency
        self.importeCot = importeCot
      
    def getid_Exchange(self):
        return self.id_Exchange

    def setid_Exchange(self,id_Exchange):
        self.id_Exchanges =id_Exchange

    def getdateCoti(self):
        return self.dateCoti

    def setdateCotit(self,dateCoti):
        self.dateCoti =dateCoti

    def getFkidCurrency(self):
        return self.FkidCurrency

    def setFkidCurrency(self,FkidCurrency):
        self.FkidCurrency =FkidCurrency

    def getImporteCot(self):
        return self.importeCot

    def setImporteCot(self,importeCot):
        self.importeCot =importeCot

    

