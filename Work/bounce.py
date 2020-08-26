# bounce.py
#
# Exercise 1.5

height = 100

for i in range(0, 10):
    height = height * 0.60
    print(i + 1, round(height, 4))