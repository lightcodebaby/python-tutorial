# Functions basics


def hello(name: str, last_name: str, age: int):
    print("Hello " + name + " " + last_name + "!")
    print("You are " + str(age) + " years old")
    print("Have a nice day!")


my_name = "Ruben"
my_last_name = "Lopez Gomez"
hello(my_name, my_last_name, 28)

# Functions arguments


def multiply(first_number, second_number):
    result = first_number * second_number
    return result


x = multiply(6, 8)
print(x)

# Functions keyword arguments


def hello_keyword_arguments(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello_keyword_arguments(
    last="Gomez", middle="Lopez", first="Ruben"
)  # Hello Ruben Lopez Gomez

# Nested functions calls

num = print(round(abs(float(input("Enter a whole positive number: ")))))

# *args


def add(*args):
    result = 0
    for item in args:
        result += item
    return result


print(add(1, 2, 3, 4, 5, 6))

# *kwargs will pack all arguments into a dictionary


def hello_kwargs(**kwargs):
    print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr", first="Ruben", middle="Lopez", last="Gomez")
