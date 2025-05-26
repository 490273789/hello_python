# turtle 使用
import turtle

def draw_square(side_length):
    """绘制一个正方形"""
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
def draw_circle(radius):
    """绘制一个圆形"""
    turtle.circle(radius)
def draw_triangle(side_length):
    """绘制一个等边三角形"""
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
def draw_star(size):
    """绘制一个五角星"""
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)  # 144度是五角星的角度
def main():
    turtle.speed(1)  # 设置绘图速度
    draw_square(100)
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()
    draw_circle(50)
    turtle.penup()
    turtle.goto(150, 0)
    turtle.pendown()
    draw_triangle(100)
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    draw_star(100)
    turtle.done()