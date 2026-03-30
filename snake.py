from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.has_turned = False
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.head = self.segments[0]
    def move(self):
        self.has_turned = False
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def turn_right(self):
        if not self.has_turned:
            if self.head.heading() == 90 or self.head.heading() == 270:
                self.head.setheading(0)
                self.has_turned = True
    def turn_left(self):
        if not self.has_turned:
            if self.head.heading() == 90 or self.head.heading() == 270:
                self.head.setheading(180)
                self.has_turned = True

    def turn_up(self):
        if not self.has_turned:
            if self.head.heading() == 0 or self.head.heading() == 180:
                self.head.setheading(90)
                self.has_turned = True
    def turn_down(self):
        if not self.has_turned:
            if self.head.heading() == 0 or self.head.heading() == 180:
                self.head.setheading(270)
                self.has_turned = True