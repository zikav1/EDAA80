class Customer:
    
    def __init__(self, customer_id: str, personal_id: str, name: str) -> None:
        self._customer_id = customer_id
        self._personal_id = personal_id
        self.name = name
    
    
    def __str__(self):
        return f'Namn: {self.name} personnummer: {self._personal_id} kundnummer: {self._customer_id}'



class Account:
    
    def __init__(self, customer_id: str, account_nbr: int) -> None:
        
        self._customer_id = customer_id
        self._account_nbr = account_nbr
        self._balance = 0
    
    def deposit(self, amount: float) -> bool:
        if amount < 0:
            return False
        
        else:
            self._balance += amount
            return True
    
    
    def withdraw(self, amount: float) -> bool:
        if amount > self._balance or amount < 0:
            return False
        
        else:
            self._balance -= amount
            return True
    
    def __str__(self):
        return f'kontonummer: {self._account_nbr}, saldo: {self._balance} ({self._customer_id})'       


a = Account('C10', 1000)
a.deposit(100)
a.withdraw(120)
print(a)




class Bank:
    
    def __init__(self):
        pass