from calendar import month
from re import X


name = "snow storm"
# print("% srm" % name[6:8])

test_dict = {}
# print(len(test_dict))


# print(r"\nHello")


test_dict = {"g": 4, "d": 3}
# print(test_dict['r'])
# print(list(test_dict.keys()))

name = ['george', 'John', 'Liam']
# print(name.concatenate("\n"))
# print("\n".join(name))


def test(): pass


# print(type(test))

list = ['f', 'f', 'f', 'f', 'f']
print(list[12:])


def test_func():
    try:
        print(1/0)
    except:
        print(3)
    finally:
        print(2)


test_func()


values = [1, 2, 1, 3]
nums = set(values)
print(nums)


def check(num):
    if num in nums:
        return True
    else:
        return False


for i in filter(check, values):
    print(i)

f = None
for i in range(5):
    with open("infile.txt", "w") as f:
        if i > 2:
            break
print(f.closed)

counter = {}


def one_more(country):
    if country in counter:
        counter[country] += 1
    else:
        counter[country] -= 1
    one_more("Honduras")
    one_more("India")
    one_more("honduras")


print(len(counter))

fruits = ['apple', 'orange', 'watermelon']

months = ['jan',
          'Feb']

# print("fruits:%s,months%s", % \(fruits, month))

a = {"2": [1, 2], '4': [3, 4]}
print(a['2'])

t = (1, 2, )
x = 2*t
t = (t, x)
print(t)

#f = open("file.txt")
t = (1, 2, 4, 3, 8, 9)
print(t[1:3])
#print([t[i] for i in range(0, len(t), 2)])

names = ['Cersei', 'Arya', 'John', 'Mao']
print(names[-1][-1])


def foo(list1):
    list1[0] = 1


test_list = [0]
foo(test_list)
print(test_list)

a = 1
b = 2
a, b = b, a
print("%d %d" % (a, b))

values = [2, 3, 2, 4]


def transformation(num):
    return num**2


for i in map(transformation, values):
    print(i)

dict = {}
dict[1] = 1
dict['1'] = 1
dict[1] += 1
print(dict)
sum = 0
for k in dict:
    print(k)
    sum += dict[k]

print(sum)

l = [1, 2, 3]


def change_list(l):
    l.append(5)
    return l


k = change_list(l)
print(l)
print(k)
result = ('\ntest1\ntest2\n').rstrip()
print(result)
print(len(result))
result = ('\ntest1\ntest2\n').strip()
print(result)
print(len(result))
result = ('\ntest1\ntest2\n').split()
print(result)
result = ('\ntest1\ntest2\n').splitlines()
print(result)

x = 0
dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
new_data = {'1': 10, '3': 30}

dic.update(new_data)
# print(dic)
#x = sum(dic.values())
# print(x)

test = (3, 4, 5, {}, [])
print(type(test))


class First(object):
    x = 1


class Second1(First):
    pass


class Second2(First):
    pass


print(First.x, Second1.x, Second2.x)
Second1.x = 2
print(First.x, Second1.x, Second2.x)
First.x = 3
print(First.x, Second1.x, Second2.x)


number_1 = 1
number_2 = "2"
number_3 = 3

sum = 0
for i in (number_1, number_2, number_3):
    if isinstance(i, int):
        sum += i
print(sum)

print(pow(12, 3))
print(12**3)

name = "Jon"
x = name.rjust(4, "A")
# print(x)
# print(type(name))

t = (1, 2, 3, [], (), {})
print(type(t))

for num in range(2):
    print(num)

for num in range(4, 6):
    print(num)
print(num)
print()


def test_func():
    try:
        return 1
    finally:
        return 2


k = test_func()
print(k)

dict = {}
dict[(1, 2, 4)] = 8
dict[(4, 2, 1)] = 10
dict[(1, 2)] = 12

sum = 0

for k in dict:
    sum += dict[k]

print(len(dict)+sum)
print()

my_dict = {'user': 'bill', 'password': 'hillary'}
print(my_dict['password'])

lst = ['spam', 'and', 'toast']
print('_'.join(lst))


def foo():
    return total + 1


total = 0
print(foo())

name = "thunder storm"
#name[8] = X
# print(name)
print()

a = [1, 2, 3, None, (), []]
a[len(a):] = [3, ]
print(len(a))

print()
def mystery_function1(p): return p*2
def mystery_function2(p): return p*3


x = 2
x = mystery_function1(x)
x = mystery_function2(x)
x = mystery_function1(x)
print(x)

foo = 0
print()


def bar():
    global foo
    foo += 1
    print(foo)


def baz():
    print(foo)


def taz():
    foo = 10
    print(foo)


bar()
print(foo)
taz()
baz()

co = 1

print()


def do():
    global co
    for i in (1, 2, 3, 4,):
        co += 1


do()
print(co)

print()


def foo(function, val):
    print(function(val))


foo(max, [1, 2, 3])
foo(min, [1, 2, 3])

print()
t = (1, 2, 4, 3)
print(t[1:-1])

names1 = ['Cersi', 'Arya', 'John', 'Mao']
#loc = names1.index("Edward")
# print(loc)

txt = "THE BEHAVIORALIST VISITS THE FACTORY"
print(txt.lower())
