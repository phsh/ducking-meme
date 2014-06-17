# _author_ Per Hedman
import unittest
from Question import Question
from QuestionGenerator import QuestionGenerator
class TestQuestion(unittest.TestCase):
	
	def setUp(self):
		self.wordList = ['kalle']
		self.question = Question('4 + 4 ?','8')
		self.generatedQuestion = QuestionGenerator.generateWordQuestion(self.wordList)

	def test_true_question(self):
		self.assertTrue(self.question.isCorrect('8'))
		self.assertTrue(self.question.isCorrect('8 '))

	def test_true_generated_question(self):
		self.assertTrue(self.generatedQuestion.isCorrect(self.generatedQuestion.answer))
		self.assertTrue(self.generatedQuestion.isCorrect(self.wordList[0]))
		
	def test_false_question(self):
		self.assertFalse(self.question.isCorrect('Kalle Anka'))
		self.assertFalse(self.question.isCorrect('9'))

if __name__  =='__main__':
	unittest.main()