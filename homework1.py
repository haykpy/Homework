# 1
import random

class strdict:
	def __init__(self, name):
		self.dict = {}
		for key in name:
			self.dict[key] = random.randint(1, 9)

	def duble_value(self):
		return set(self.dict.values())

	def tree_max_value(self):
		return sorted(list(self.dict.values()))[-3:]

dict_1 = strdict("python")
print(dict_1.dict)
print(dict_1.duble_value())
print(dict_1.tree_max_value())

# -------------------------------------------------
# 2
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())