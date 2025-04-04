print("Welcome to my world!")
import pyfiglet

text = "Welcome!"
text=pyfiglet.print_figlet(text="Welcome",
                           colors='Blue')




name = input("Would you mind sharing you name with us?")
print(f"Greetings! {name} Nice to meet you there!")
age = input("How old are you?")
age_100 = 100 - int(age) + 2025
print(f"You will be 100 years old in {age_100}")


answer_01 = input("Do you watch Anime? (Yes/No):")
if answer_01 == "Yes":
    print("Wow,amazing didnt expect you there!")
else:
    print("Oh i see,but you should!")

answer_02 = input("Have you been well lately? (Yes/No/Don't wanna share):")
if answer_02 == "Yes":
    print("Glad to hear that man!")
elif answer_02 == "No":
    print("Aww it's fine,i hope everything will be good!")
else:
    print("It's fine.But i just wanna say you're perfect the way you are ""wink wink")

import pyfiglet

text = "Love you!"
text=pyfiglet.print_figlet(text="Love you!",
                           colors='Red')













import turtle
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    turtle.setup(width=800, height=600)
    turtle.bgcolor("white")
    
    turtle.penup()
    turtle.speed(2)

    draw_circle("yellow", 150, 0, -150)

    draw_circle("black", 20, -50, 30)
    draw_circle("black", 20, 50, 30)

    draw_circle("white", 5, -50, 30)
    draw_circle("white", 5, 50, 30)

    turtle.penup()
    turtle.goto(-65, -15)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(75, 130)

    turtle.hideturtle()
    turtle.exitonclick()


    