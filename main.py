from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.tracer(0)


screen.listen()
screen.onkeypress(fun=snake.turn_left, key="a")
screen.onkeypress(fun=snake.turn_right, key="d")
screen.onkeypress(fun=snake.turn_up, key="w")
screen.onkeypress(fun=snake.turn_down, key="s")
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)


    snake.move()


    if  snake.head.distance(food) < 15:
        scoreboard.add_score()
        food.refresh()



screen.exitonclick()