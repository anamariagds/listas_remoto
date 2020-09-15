def turtle(l):
    from turtle import *

    shape("turtle")
    speed(4)
    color("#DA70D6")
    pensize(5)

    for volta in range(l):
        forward(100)
        right(45)
def main():
    turtle(8)

done()
