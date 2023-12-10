import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

Screen = Screen()
Screen.setup(width=600,height=600)
Screen.bgcolor("Black")
Screen.title("My Snake Game")
Screen.tracer(0)


snake= Snake()
food=Food()
scoreboard=Scoreboard()

Screen.listen()
Screen.onkey(snake.up,"Up")
Screen.onkey(snake.down,"Down")
Screen.onkey(snake.left,"Left")
Screen.onkey(snake.right,"Right")

game_is_on= True
while game_is_on:
    Screen.update()
    time.sleep(0.1)


    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()


    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()




Screen.exitonclick()