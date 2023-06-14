def hello():
    print("Hello")


print(hello)  # memory address

hi = hello
print(hi)  # same memory address

hi()

say = print
say("Hello World!")
