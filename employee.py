class Contract:
    def __init__(self, numOfContracts, rate) -> None:
        self.description = f"commission for {numOfContracts} contract(s) at {rate}/contract"
        self.value = numOfContracts * rate

class Fixed:
    def __init__(self, bonus) -> None:
        self.description = f"bonus commission of {bonus}"
        self.value = bonus

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        return self.get_base_pay() + (self.commission.value if self.commission else 0)

    def __str__(self):
        return f"{self.name} works on a {self.get_contract_desc()}" + \
            (f" and receives a {self.commission.description}" if self.commission else "") + \
                f". Their total pay is {self.get_pay()}."

class Salaried(Employee):
    def __init__(self, name, salary, commission=None):
        super().__init__(name, commission)
        self.salary = salary

    def get_contract_desc(self):
        return f"monthly salary of {self.salary}"

    def get_base_pay(self):
        return self.salary

class Hourly(Employee):
    def __init__(self, name, hours, pay_per_hour, commission=None):
        super().__init__(name, commission)
        self.hours = hours
        self.pay_per_hour = pay_per_hour

    def get_contract_desc(self):
        return f"contract of {self.hours} hours at {self.pay_per_hour}/hour"

    def get_base_pay(self):
        return self.hours * self.pay_per_hour

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salaried("Billie", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly("Charlie", 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salaried("Renee", 3000, Contract(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly("Jan", 150, 25, Contract(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salaried("Robbie", 2000, Fixed(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly("Ariel", 120, 30, Fixed(600))
