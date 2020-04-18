class Sweetmenu:
    menu={}
    def test(self,name,price):
        self.name=name
        self.price=price
        self.menu[self.name]=self.price
    def display(self):
        print(self.menu)
    pass

sweet_menu=Sweetmenu()

n=int(input('Enter the no. of items you want to add in your menu'))
for i in range(0,n):
    sweet_menu.name=str(input('Enter the name of the sweet'))
    sweet_menu.price=int(input('Enter the price you want to desginate to the sweet'))
    sweet_menu.test(sweet_menu.name,sweet_menu.price)
    print(str(sweet_menu.name)+' will cost you around '+str(sweet_menu.price)+' Dollars')
sweet_menu.display()
      
