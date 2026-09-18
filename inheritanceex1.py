class animal():
  def eat(self):
    print("animal is eating")
class dog(animal):
  def walk(self):
    print("dog is barking")
d1=dog()
d2=dog()
an=animal()
d1.walk()
d1.eat()
