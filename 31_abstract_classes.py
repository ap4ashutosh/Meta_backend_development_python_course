from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        a = input("How much you would like to donate: ")
    
amounts = []
john = Donation()
j = john.donate()
amounts.appenda(j)

peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)