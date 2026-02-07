

# Example with a more specific exception
class InsufficientFundsError(Exception):
    """Raised when account balance is insufficient"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds: balance {balance}, requested {amount}"
        super().__init__(self.message)



# Usage example
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


# Try-except example
try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Error: {e}")