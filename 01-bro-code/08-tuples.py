# A tuple is a collection which is ordered and unchangeable

student = ("Ruben", 28, "male")

print(student.count("Ruben"))  # 1
print(student.index("male"))  # 2

for x in student:
    print(x)  # Ruben, 28, male

if "Ruben" in student:
    print("Ruben is here!")
