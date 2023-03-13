import time
from turtle import Turtle # 클래스 명은 맨 앞 글자가 대문자.

john = Turtle()
print(john)

john.shape("turtle")
john.color("red", "green")
while True:
    john.forward(5)
    john.left(5)
    time.sleep(1)