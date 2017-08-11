#!/usr/bin/python3

# if语句检查current_number与2的求模运算结果。如果结果为0（意味着current_number可被2整除），就执行continue语句，让Python忽略余下的代码，并返回到循环的开头

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# 避免无限循环

x = 1
while x <= 5:
    print(x)
    x += 1
