class Graphics:
    def __init__(self,month: int, fee :int):
        self.month = month
        self.fee = fee

    def get_month(self) -> int:
        return self.month
    
    def set_month(self, month: int) -> None:
        self.month = month
    
    def get_fee(self) -> int:       
        return self.fee
    
    def set_fee(self, fee: int) -> None:
        self.fee= fee 
    
 