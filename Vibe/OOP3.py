class Circle:
  def __init__(self,r):
    self.r = r
  
  def Area(self):
    return 3.14*self.r*self.r

  def Perimeter(self):
    return 2*3.14*self.r

c = Circle(12)
print(c.Area())
print(c.Perimeter())

class Employee:
  def __init__(self,role,department,salary):
    self.department = department
    self.salary = salary
    self.role = role
  
  def showDetails(self):
    print("Role :",self.role)
    print("Department :",self.department)
    print("Salary :",self.salary)
    print("------------------------------")

e = Employee("SDE","Development",100000)
e.showDetails()

class Engineer(Employee):
  def __init__(self,name,age):
    self.name = name
    self.age = age
    super().__init__("DevOps","SRE",1800000)

e2 = Engineer("Pranav",34)
e2.showDetails()


class Order:
  def __init__(self,item,price):
    self.item = item
    self.price = price

  def __gt__(self,other):
      return self.price > other.price
       
i = Order("Pizza",1000)
j = Order("Burger",200)
print(i>j)
print(j>i)
