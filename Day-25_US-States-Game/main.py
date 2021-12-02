import turtle
import pandas

FONT = ("Ariel", 14, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# # My try
# answer_state = []
# correct_state = turtle.Turtle()
# correct_state.hideturtle()
# correct_state.penup()
# correct = 0
# already_there = True
#
# while len(answer_state) < 50:
#     guess = str((screen.textinput(title=f"{correct} States guessed correctly", prompt="What's another state's name"))).lower()
#
#     for state in states_data["state"]:
#
#         for guessed_state in answer_state:
#             if guessed_state == guess:
#                 already_there = True
#             else:
#                 guessed_state = False
#
#         if state == guess:
#             if not already_there:
#                 answer_state.append(guess)
#                 correct_state.write(f"{guess}.title()", font=FONT)
#                 correct_state.goto(answer_state[answer_state[state]].x, answer_state[answer_state[state]].y)
#                 correct += 1
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct States",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# # states_to_learn.csv
# states_to_learn_dict = {"States to learn": []}
# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn_dict["States to learn"].append(state)
#
# pandas.DataFrame(states_to_learn_dict).to_csv("states_to_learn.csv")



# turtle.mainloop()
# screen.exitonclick()
