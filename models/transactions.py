class Transactions:
    def __init__(self, id_accounting_transactions: int, fkid_v_account: int, fkid_sub_account: int, fkid_v_increased_by: int,
                 accrued_date: str, amount: float, fkid_country: int, fkid_city: int, comment: str, fkid_dues: int) -> None:
        self.id_accounting_transactions = id_accounting_transactions
        self.fkid_v_account = fkid_v_account
        self.fkid_sub_account = fkid_sub_account
        self.fkid_v_increased_by = fkid_v_increased_by
        self.accrued_date = accrued_date
        self.amount = amount
        self.fkid_country = fkid_country
        self.fkid_city = fkid_city
        self.comment = comment
        self.fkid_dues = fkid_dues

    def get_id_accounting_transactions(self) -> int:
        return self.id_accounting_transactions

    def set_id_accounting_transactions(self, value: int) -> None:
        self.id_accounting_transactions = value

    def get_fkid_v_account(self) -> int:
        return self.fkid_v_account

    def set_fkid_v_account(self, value: int) -> None:
        self.fkid_v_account = value

    def get_fkid_sub_account(self) -> int:
        return self.fkid_sub_account

    def set_fkid_sub_account(self, value: int) -> None:
        self.fkid_sub_account = value

    def get_fkid_v_increased_by(self) -> int:
        return self.fkid_v_increased_by

    def set_fkid_v_increased_by(self, value: int) -> None:
        self.fkid_v_increased_by = value

    def get_accrued_date(self) -> str:
        return self.accrued_date

    def set_accrued_date(self, value: str) -> None:
        self.accrued_date = value

    def get_amount(self) -> float:
        return self.amount

    def set_amount(self, value: float) -> None:
        self.amount = value

    def get_fkid_country(self) -> int:
        return self.fkid_country

    def set_fkid_country(self, value: int) -> None:
        self.fkid_country = value

    def get_fkid_city(self) -> int:
        return self.fkid_city

    def set_fkid_city(self, value: int) -> None:
        self.fkid_city = value

    def get_comment(self) -> str:
        return self.comment

    def set_comment(self, value: str) -> None:
        self.comment = value

    def get_fkid_dues(self) -> int:
        return self.fkid_dues

    def set_fkid_dues(self, value: int) -> None:
        self.fkid_dues = value