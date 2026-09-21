ass Product:
  def __init__(self,name,price):
    self.name=name
    self.price=price
  def display_product(self):
    print("product name",self.name)
    print("product price",self.price)
  def calculate_discount(self):
    discount=self.price*5/100
    final_price = self.price - discount
    print("discount price",final_price)
  
class Electronics(Product):
  def __init__(self,name,price,warranty_years):
    super().__init__(name,price)
    self.warranty_years=warranty_years
    print("warranty",warranty_years)
  def calculate_discount(self):
    discount=self.price*10/100
    final_price = self.price - discount
    print("discount price",final_price)

class Clothing(Product):
  def __init__(self,name,price,size):
    super().__init__(name,price)
    self.size=size
  def calculate_discount(self):
    discount=self.price*20/100
    final_price = self.price - discount
    print("Discount price",final_price)
c=Clothing("tops",2000,38)
c.display_product()
c.calculate_discount()

e=Electronics("charger",1200,10)
e.display_product()
e.calculate_discount()

  
    
