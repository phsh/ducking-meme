# _author_ Per Hedman
import unittest

class Question:
	
	def __init__(self, question, answer, level = 0):
		self.question = question
		self.answer = answer
		self.level = level

	def isCorrect(self, my_answer):
		return self.answer.lower().strip() == my_answer.lower().strip()