class Customer:
    def __init__(self, identity, fullname):
        self._fullname = fullname
        self._identity = identity
        self._accounts = []

    @property
    def identity(self):
        return self._identity

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        self._fullname = fullname

    @property
    def accounts(self):
        return self._accounts

    def add_account(self, account):
        self._accounts.append(account)

    def remove_account(self, account):
        self._accounts.remove(account)

    def get_account(self, iban):
        for account in self.accounts:
            if account.iban == iban:
                return account
        return None


