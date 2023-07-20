from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

BOUNDING_BOX = 280
#Screen creation and setup
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	#Detect collision with food
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.increase_score()

	#Detect collision with the wall
	if abs(snake.head.xcor()) > BOUNDING_BOX or abs(snake.head.ycor()) > BOUNDING_BOX:
		scoreboard.reset()
		snake.reset()

	#Detect collision with the tail
	for segment in snake.segments:
		if segment == snake.head:
			pass
		elif snake.head.distance(segment) < 10:
			scoreboard.reset()
			snake.reset()
screen.exitonclick()
