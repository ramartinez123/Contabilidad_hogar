class Ledger:
    def __init__(self, fkid_v_account: int, account: str, january: int, february: int, march: int, april: int,
                 may: int, june: int, july: int, august: int, september: int, october: int, november: int,
                 december: int) -> None:
        self.fkid_v_account = fkid_v_account
        self.account = account
        self.january = january
        self.february = february
        self.march = march
        self.april = april
        self.may = may
        self.june = june
        self.july = july
        self.august = august
        self.september = september
        self.october = october
        self.november = november
        self.december = december

    def get_fkid_v_account(self) -> int:
        return self.fkid_v_account

    def set_fkid_v_account(self, value: int) -> None:
        self.fkid_v_account = value

    def get_account(self) -> str:
        return self.account

    def set_account(self, value: str) -> None:
        self.account = value

    def get_january(self) -> int:
        return self.january

    def set_january(self, january: int) -> None:
        self.january = january

    def get_february(self) -> int:
        return self.february

    def set_february(self, february: int) -> None:
        self.february = february

    def get_march(self) -> int:
        return self.march

    def set_march(self, march: int) -> None:
        self.march = march

    def get_april(self) -> int:
        return self.april

    def set_april(self, april: int) -> None:
        self.april = april

    def get_may(self) -> int:
        return self.may

    def set_may(self, may: int) -> None:
        self.may = may

    def get_june(self) -> int:
        return self.june

    def set_june(self, june: int) -> None:
        self.june = june

    def get_july(self) -> int:
        return self.july

    def set_july(self, july: int) -> None:
        self.july = july

    def get_august(self) -> int:
        return self.august

    def set_august(self, august: int) -> None:
        self.august = august

    def get_september(self) -> int:
        return self.september

    def set_september(self, september: int) -> None:
        self.september = september

    def get_october(self) -> int:
        return self.october

    def set_october(self, october: int) -> None:
        self.october = october

    def get_november(self) -> int:
        return self.november

    def set_november(self, november: int) -> None:
        self.november = november

    def get_december(self) -> int:
        return self.december

    def set_december(self, december: int) -> None:
        self.december = december