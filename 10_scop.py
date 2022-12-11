# global scope
my_global = 10

def func1():
    #enclosed variable
    enclosed_var = 5
    def func2():
        #local variable
        var_local = 13
        print("Access to global ", my_global)
        print("access to enclosed ", enclosed_var)
    func2()
    

func1()
print("can't access local variable", "var_local")
# Here it will show an error as var_local is declared locally and can't be accessed outside that function

