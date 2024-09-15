class Account:
    def __init__(self, id_account: int, account: str, fkid_v_account_type: int, fkid_accounting_item: int,
                 fkid_v_increased_by: int, fkid_accounting_method: int, fkid_currency: int, detalle: str) -> None:
        self.id_account = id_account
        self.account = account
        self.fkid_v_account_type = fkid_v_account_type
        self.fkid_accounting_item = fkid_accounting_item
        self.fkid_v_increased_by = fkid_v_increased_by
        self.fkid_accounting_method = fkid_accounting_method
        self.fkid_currency = fkid_currency
        self.detalle = detalle

    def get_id_account(self) -> int:
        return self.id_account

    def set_id_account(self, value: int) -> None:
        self.id_account = value

    def get_account(self) -> str:
        return self.account

    def set_account(self, value: str) -> None:
        self.account = value

    def get_fkid_v_account_type(self) -> int:
        return self.fkid_v_account_type

    def set_fkid_v_account_type(self, value: int) -> None:
        self.fkid_v_account_type = value

    def get_fkid_accounting_item(self) -> int:
        return self.fkid_accounting_item

    def set_fkid_accounting_item(self, value: int) -> None:
        self.fkid_accounting_item = value

    def get_fkid_v_increased_by(self) -> int:
        return self.fkid_v_increased_by

    def set_fkid_v_increased_by(self, value: int) -> None:
        self.fkid_v_increased_by = value

    def get_fkid_accounting_method(self) -> int:
        return self.fkid_accounting_method

    def set_fkid_accounting_method(self, value: int) -> None:
        self.fkid_accounting_method = value

    def get_fkid_currency(self) -> int:
        return self.fkid_currency

    def set_fkid_currency(self, value: int) -> None:
        self.fkid_currency = value

    def get_detalle(self) -> str:
        return self.detalle

    def set_detalle(self, value: str) -> None:
        self.detalle = value