# Найти результат выражения для произвольных значений a,b: (a2 + b2) % 2
import random
a = random.randint(1, 99)
b = random.randint(1, 99)
answer = (a**2 + b**2) % 2
print("If a = {0} and b = {1}.".format(a, b), "\nThe answer is: {0:.2f}".format(answer))
