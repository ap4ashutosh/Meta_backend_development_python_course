class Payslips():
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "Yes"

    def status(self):
        if self.payment == "Yes":
            return f"{self.name} has been paid with {self.amount}"
        else:
            return f"{self.name} has not been paid yet"
ravi = Payslips("Ravi", "Yes", 17000)
sikandar = Payslips("Sikandar", "No", 15000)
kumar = Payslips("Raghunath", "No", 12000)

print("Before payment")
print(ravi.status()+'\n'+sikandar.status()+'\n'+kumar.status())

sikandar.pay()
print("after payment")
print(ravi.status()+'\n'+sikandar.status()+'\n'+kumar.status())
