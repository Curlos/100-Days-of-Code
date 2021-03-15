from state_name import State

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

gameIsOn = True
correctStates = {}

states = pandas.read_csv("50_states.csv")
allStates = (states["state"].to_dict().values())

while len(correctStates) < 50:
    guess = screen.textinput(title=f"{len(correctStates)}/50 States Correct",
                             prompt="What's another state's name?")
    guess = guess.title()
    if guess == "Exit":
        break
    if len(states[states["state"] == f"{guess}"]) == 1:
        if guess not in correctStates:
            state = states[states["state"] == f"{guess}"]
            stateName = guess
            x = int(state.x)
            y = int(state.y)
            correctStates[stateName] = (x, y)

            newState = State(stateName, "black", x, y)

if len(correctStates) == 50:
    print('You have guessed every state correctly!')
elif len(correctStates) < 50:
    missingStates = {'state': [],
                     'x': [],
                     'y': []}
    for state in allStates:
        if state not in correctStates:
            s = states[states["state"] == f"{state}"]
            x = int(s.x)
            y = int(s.y)

            newState = State(state, "red", x, y)

            missingStates['state'].append(state)
            missingStates['x'].append(x)
            missingStates['y'].append(y)

    missingStatesData = pandas.DataFrame(missingStates)
    missingStatesData.to_csv("missing_states.csv")

screen.exitonclick()
