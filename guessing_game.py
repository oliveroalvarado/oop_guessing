import random

class GuessingGame():
  
    def __init__(self, answer):
        self.answer = answer
        self.last_guess = None
        self.last_result = None
    
    def sovled(self):
        return self.last_result == "correct"
    
    def guess(self, user_guess):
        self.last_guess = user_guess
        if user_guess == self.answer:
            self.last_result = "correct"
        elif user_guess < self.answer:
            self.last_result = "too low"
        else:
            self.last_result = "too high"
        return self.last_result
    