# _author_ Per Hedman
import unittest

class Question:
	
	def __init__(self, question, answer, level = 0):
		self.question = question
		self.answer = answer
		self.level = level

	def isCorrect(self, my_answer):
		return self.answer.lower().strip() == my_answer.lower().strip()

class TestQuestion(unittest.TestCase):
	def setUp(self):
		self.question = Question('4 + 4 ?','8')

	def test_true_question(self):
		self.assertTrue(self.question.isCorrect('8'))
		self.assertTrue(self.question.isCorrect('8 '))

	def test_false_question(self):
		self.assertFalse(self.question.isCorrect('Kalle Anka'))
		self.assertFalse(self.question.isCorrect('9'))

if __name__  =='__main__':
	unittest.main()
