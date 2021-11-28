class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_input = input(f"Q.{self.question_number + 1} {self.question_list[self.question_number].text}"
                           f" (True / False)? : ")
        self.check_answer(user_input, self.question_list[self.question_number].answer)
        self.question_number += 1
        print(f"Your score is {self.score}/{self.question_number}")

    def check_answer(self, user_input, answer):
        if user_input.lower() == answer.lower():
            print("You're right!")
            self.score += 1
        else:
            print("You're wrong.")
        print(f"The correct answer is {answer}\n")



