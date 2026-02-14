# Quiz Game Application

## Description
This is a simple console-based quiz game application where users can answer multiple-choice questions.

## Features
- Multiple choice questions
- Score tracking
- User-friendly interface

## Code
```python
import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['Berlin', 'Madrid', 'Paris', 'Lisbon'],
                'answer': 'Paris'
            },
            {
                'question': 'What is 2 + 2?',
                'options': ['3', '4', '5', '6'],
                'answer': '4'
            },
            {
                'question': 'What is the color of the sky?',
                'options': ['Blue', 'Green', 'Red', 'Yellow'],
                'answer': 'Blue'
            }
        ]
        self.score = 0

    def ask_question(self, question):
        print(question['question'])
        for idx, option in enumerate(question['options']):
            print(f"{idx + 1}. {option}")
        answer = input('Select an option: ')
        if question['options'][int(answer) - 1] == question['answer']:
            print('Correct!')
            self.score += 1
        else:
            print('Wrong!')

    def run(self):
        for question in self.questions:
            self.ask_question(question)
        print(f'Your total score is: {self.score}/{len(self.questions)}')

if __name__ == '__main__':
    game = QuizGame()
    game.run()
```