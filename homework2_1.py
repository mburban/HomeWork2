# Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )
import random
a = random.randint(1, 99)
b = random.randint(1, 99)
c = random.randint(1, 99)
answer = a + b * (c / 2)
print("If a = {0}, b = {1} and c = {2}.".format(a, b, c), "\nThe answer is: {0:.2f}".format(answer))
