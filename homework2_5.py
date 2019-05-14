# Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )
import random
import math
a = random.randint(1, 99)
b = random.randint(1, 99)
c = random.randint(1, 99)
answer = math.fabs(a - b) / (a + b)**3 - math.cos(c)
print("If a = {0}, b = {1} and c = {2}.".format(a, b, c), "\nThe answer is: {0:.2f}".format(answer))
