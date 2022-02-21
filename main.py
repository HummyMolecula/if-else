from ast import If
import random as ran

data = int(input("Enetr number: "))
random = ran.randint(0, 100)
print("Random number:", random)

if data == random:
    print("You are right!")
elif data <= 0:
    print(data, "too small!")
elif data >= 100:
    print(data, "too big!")
else:
    print("Try again!")
