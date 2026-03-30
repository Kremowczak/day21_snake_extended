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
    def move(self):
        self.has_turned = False
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def turn_right(self):
        if not self.has_turned:
            if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
                self.segments[0].setheading(0)
                self.has_turned = True
    def turn_left(self):
        if not self.has_turned:
            if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
                self.segments[0].setheading(180)
                self.has_turned = True

    def turn_up(self):
        if not self.has_turned:
            if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
                self.segments[0].setheading(90)
                self.has_turned = True
    def turn_down(self):
        if not self.has_turned:
            if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
                self.segments[0].setheading(270)
                self.has_turned = True