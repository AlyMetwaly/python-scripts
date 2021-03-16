r = range(0, 30)
print(type(r))
print(type(10))
print(type('a'))
print(type("Hi there"))


class Car:
    pass


class Truck(Car):
    pass


# c is a direct instace (object) of truck
c = Car()
convert = Car()
# t is a direct instace (object) of truck, even tho that truck inherits from car
t = Truck()
print(type(c))
print(type(t))
# type checks for direct instance and not interitance
print(type(c) == type(t))
print(type(c) == type(convert))

# isinstance takes one object and one class info. ininstance accounts for both direct instance, as well as, inheritance
print(isinstance(c, Car))
print(isinstance(t, Car))

if isinstance(r, range):
    print(list(r))
