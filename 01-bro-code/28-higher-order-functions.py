# higher order function:
# 	1. accepts a function as an argumen
# 	2. returns a function


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    print(func("Hello"))


hello(loud)  # HELLO
hello(quiet)  # hello

# ------


def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(2)  # it returns the function without calling it
print(divide(10))  # 5
