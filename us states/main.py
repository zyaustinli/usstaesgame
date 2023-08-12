import turtle
import pandas

data = pandas.read_csv(r"C:\udemy projects\us states\50_states.csv")

screen= turtle.Screen()
img = r"C:\udemy projects\us states\blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

states = data.state.to_list()
guessed=[]

while len(guessed)<50:

    answer= screen.textinput(f"{len(guessed)}/50 states", "What's another state's name? ").title()
    

    if answer== "Exit":
        missing = []
        for state in states:
            if state not in guessed:
                missing.append(state)

        new_data = pandas.DataFrame(missing)
        new_data.to_csv(r"C:\udemy projects\us states\states_to_learn.csv")
        break

    if answer in states:
        guessed.append(answer)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


