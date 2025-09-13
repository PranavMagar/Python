class Complex:
  def __init__(self,real,img):
    self.real = real
    self.img = img

  def shownum(self):
    print(self.real,"i","+",self.img,"j")

  def __sub__(self,num2):
    self.real = self.real - num2.real
    self.img = self.img - num2.img
    return Complex(self.real,self.img)

  def __add__(self,num2):
    self.real = self.real + num2.real
    self.img = self.img + num2.img
    return Complex(self.real,self.img)

num = Complex(2,3)
num.shownum()

num2 = Complex(4,5)
num2.shownum()

num3 = num - num2
num3.shownum()

num4 = num + num2
num4.shownum()
