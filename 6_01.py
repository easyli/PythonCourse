#!/usr/bin/python3

# user.py

# 注意，即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。

# 遍历所有的 键—值对  最先打印的是 'last'

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey " + key)
    print("Value " + value)
