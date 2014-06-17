# _author_ Per Hedman
import unittest
from Question import Question
from QuestionGenerator import QuestionGenerator

class TestQuestion(unittest.TestCase):
	wordList = ['kalle']	
		
	def test_question_true(self):
		question = Question('4 + 4 ?','8')
		self.assertTrue(question.isCorrect('8'))
		self.assertTrue(question.isCorrect('8 '))
		self.assertTrue(question.isCorrect(question.answer));

	def test_false_question(self):
		question = Question('4 + 4 ?','8')
		self.assertFalse(question.isCorrect('Kalle Anka'))
		self.assertFalse(question.isCorrect('9'))

	def test_generate_word_question_true(self):
		generatedQuestion = QuestionGenerator.generateWordQuestion(self.wordList)
		self.assertTrue(generatedQuestion.isCorrect(generatedQuestion.answer))
		self.assertTrue(generatedQuestion.isCorrect(self.wordList[0]))

	def test_generate_word_question_false(self):
		generatedQuestion = QuestionGenerator.generateWordQuestion(self.wordList)
		self.assertFalse(generatedQuestion.isCorrect(''))
		self.assertFalse(generatedQuestion.isCorrect('22'))		

	def test_generate_math_question_true(self):
		question = QuestionGenerator.generateMathQuestion(1,1)
		self.assertTrue(question.isCorrect('2'))

	def test_generate_math_question_false(self):
		question = QuestionGenerator.generateMathQuestion(1,1)
		self.assertTrue(question.isCorrect('2'))

if __name__  =='__main__':
	unittest.main()