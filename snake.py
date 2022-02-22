# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 22:07:24 2022

@author: Robel
"""
from turtle import Screen, Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_Snake()
        self.head = self.segments[0]
        
        
        
    def create_Snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("White")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x_cor = self.segments[seg_num-1].xcor()
            y_cor = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)        
            

        self.head.forward(MOVE_DISTANCE)
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)