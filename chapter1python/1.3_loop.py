import random

answer = random.randint(1,100)
guess = 0

while guess != answer:
    guess = int(input("1~100猜一个"))
    if guess > answer:
        print("太大了")
    elif guess < answer:
        print("太小了")

print("猜对了")