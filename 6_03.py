#!/usr/bin/python3

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# 按顺序遍历字典中的所有键

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 遍历字典中的所有值

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 集合类似于列表，但每个元素都必须是独一无二的
# 用集合可以剔除相同元素

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
      print(language.title())
