def hello(name):
    print("Hello there " + name)

hello("Bob")



cars = ['tesla','ford','chevy','volvo']

cars.sort(reverse=True)

for i in cars:
    print(i)

x= cars.count('chevy')


print(x)


y = lambda x: x**x

print(y(4))

fname="carter"
lname="thurman"

print("Hello {} {}, welcome to Python!".format(fname,lname))

print("binary: {0:b}".format(52))

def getSum(num1,num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))


getSum(2,4)

myAdd=getSum

myAdd(2,4)
