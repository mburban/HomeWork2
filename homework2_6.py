# Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )4 + | a |
import random
import math
a = random.randint(1, 99)
b = random.randint(1, 99)
c = random.randint(1, 99)
answer = (math.log(1 + c) / -b)**4 + math.fabs(a)
print("If a = {0}, b = {1} and c = {2}.".format(a, b, c), "\nThe answer is: {0:.2f}".format(answer))
