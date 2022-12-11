class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print('The ' + self.dish + ' has ' + str(self.items) + ' and takes ' + str(self.time) + ' minutes to prepare')


pizza = Recipe('Pizza', ['bread', 'cheese', 'tomato'], 45)
pasta = Recipe('Pasta', ['penne', 'sauce'], 55)
biryani = Recipe('Biryani', ['rice', 'meat', 'spices', 'curd', 'salad'], 60)

print(pizza.items)
print(pasta.items)
print(biryani.items)

print(pizza.contents())
