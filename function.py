def mitmorn():
    print("This is MIT morning class")


mitmorn()


def square(num):
    return num ** 2


object_ = square(8)
print("the square of the given number is:", object_)


def calculate():
    x = 7
    y = 8
    print(x * y)
    print(x + y)


calculate()


def majina(myfirstname, mylastname, age):
    print("Am", myfirstname + "" + mylastname, "and I am", age, "years old")


majina("Daniel", " Toosie", 18)
majina('Erick', ' Ondara', 19)
majina('wayne', ' kwame', 20)


# CREATE A FUNCTION TO CALCULATE THE AVERAGE OF A LIST OF NUMBERS
# (2.5,6,3,5)

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


data = [3, 4, 6, 8, 6, 9]
result= calculate_average(data)
print("The average is ",result)

#create a function that gives you the longest string in a list
