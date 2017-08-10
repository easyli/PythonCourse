#!/usr/bin/python3

# squares.py

squares = [value**2 for value in range(1,11)]
print(squares)

# ------以下的代码同样的打印,但是很罗嗦 -------

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
