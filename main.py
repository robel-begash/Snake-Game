# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 19:12:37 2022
steps
-create snake body
-move the snake
-control the snake
-detect collision with food
-create a score board
-detect collision with thewall
@author: Robel
"""
from turtle import Screen, Turtle
from snake import Snake
import time
sc = Screen()
sc.setup(width = 600, height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
is_game_on = True

sc.tracer(0)



snake = Snake()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")



while is_game_on:
    sc.update()
    time.sleep(0.1)
    
    snake.move()    
    


sc.exitonclick()
sc.bye()

