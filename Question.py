# _author_ Per Hedman
import unittest

class Question:
	
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

	def isCorrect(self, my_answer):
		return self.answer.lower().strip() == my_answer.lower().strip()

class MathQuestion(Question):
	def __init__(self,question,answer):
		Question.__init__(self,question,answer)

class WordQuestion(Question):
	def __init__(self,question,answer):
		Question.__init__(self,question,answer)	
