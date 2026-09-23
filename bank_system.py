class BankAccount:
    def __init__(self, account_holder, initial_deposit=0.0):
        self.account_holder = account_holder

        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        self._balance = initial_deposit
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        self._balance += amount
        self._transactions.append(f"Deposited: {amount}")

        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if self._balance < amount:
            raise ValueError("Insufficient balance.")

        self._balance -= amount
        self._transactions.append(f"Withdrew: {amount}")

        return amount

    def get_transaction_history(self):
        return self._transactions.copy()


class ATM:
    def __init__(self, bank_account):
        self._bank_account = bank_account
        self.__pin = "1234"
        self._is_authenticated = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self._is_authenticated = True
            return True
        else:
            self._is_authenticated = False
            return False

    def check_balance(self):
        if not self._is_authenticated:
            raise PermissionError("Authentication required.")
        return self._bank_account.balance

    def deposit(self, amount):
        if not self._is_authenticated:
            raise PermissionError("Authentication required.")
        return self._bank_account.deposit(amount)

    def withdraw(self, amount):
        if not self._is_authenticated:
            raise PermissionError("Authentication required.")
        return self._bank_account.withdraw(amount)

    def print_mini_statement(self):
        if not self._is_authenticated:
            print("Please authenticate first.")
            return

        transactions = self._bank_account.get_transaction_history()

        print("Last 3 Transactions:")

        for transaction in transactions[-3:]:
            print(transaction)

if __name__ == "__main__":
    account = BankAccount("John Doe", 1000.0)
    atm = ATM(account)

    if atm.authenticate("1234"):
        print(f"Current Balance: {atm.check_balance()}")
        atm.deposit(500.0)
        print(f"Balance after deposit: {atm.check_balance()}")
        atm.withdraw(200.0)
        print(f"Balance after withdrawal: {atm.check_balance()}")
        atm.print_mini_statement()
    else:
        print("Authentication failed.")
            
            