class Shape:
    def __init__(self, attrs):
    	self.attrs = name
    	return self.name

    def present_shape(self):

        return f"shape is {self.name}"


class Triangle(Shape):
	def __init__(self, side1, side2, base, height):
		self.side1 = side1
		self.side2 = side2
		self.base = width
		self.height = length


	def present(self):
        return F"{self.present_shape()},\
         side1 = {self.side1}, side2 = {self.side2},\
         width = {self.base} length = {self.height}"

    def area(self):

        area = (self.height * self.base * 1/2)
        return f"area is = {area}"

    def perimeter(self):

        perimeter = self.side1 + self.side2 + self.base
        return f"perimeter is = {perimeter}"
        

	
class Square(Shape):
	def __init__(self,side):

        self.side = side

    def present(self):
        return self.present_shape(), {self.side}

    def area(self):
        return f"area is = {self.side ** 2}"

    def perimeter(self):
        return f"perimeter is = {self.side * 4}"

    def diagonal(self):
        return f"diagonal = {self.side * (2 ** 1/2)}"



shape_1 = Shape("hayk")
triangle_1 = Triangle("triangle", 6, 7, 9, 8)
square_1 = Square("square", 8)


print(shape_1.present_shape())
# -----------------------------------
print(triangle_1.present())
print(triangle_1.area())
print(triangle_1.perimeter())
# -----------------------------------
print(square_1.present())
print(square_1.area())
print(square_1.perimeter())
print(square_1.diagonal())

		
# --------------------------------------------------------------------------------------------------

# class Country:
# 	def __init__(self, name,continent):
# 		self.country_name = name
# 		self.continent = continent
# 		return self.name

# class Brand:
# 	def brand_name(self):
# 		self.name = name_1

# 	def business_start_date(self):
# 		self.date = date

# 	def presentation(self):
# 		self.presentation = pres


# class Season:
# 	pass

