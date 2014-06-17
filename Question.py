# _author_ Per Hedman
import unittest
from random import shuffle
from random import randint
from random import choice

class Question:
	
	def __init__(self, question, answer, level = 0):
		self.question = question
		self.answer = answer
		self.level = level

	def isCorrect(self, my_answer):
		return self.answer.lower().strip() == my_answer.lower().strip()

class QuestionGenerator:
	@classmethod
	def generateMathQuestion(self,start_base, end_base):
		value_a = randint(start_base , end_base)
		value_b = randint(start_base , end_base)
		question = " %s + %s ? " % (value_a, value_b)
		answer = str(value_a+value_b)
		return Question(question,answer)
	@classmethod
	def generateWordQuestion(self,list_of_words):
		answer = choice(list_of_words)
		word = list(answer)
		shuffle(word)
		result = " ".join(word)
		question = " " + result + " ? " 
		return Question(question, answer)



class TestQuestion(unittest.TestCase):
	wordList = ['kalle']
	def setUp(self):
		self.question = Question('4 + 4 ?','8')
		self.generatedQuestion = QuestionGenerator().generateWordQuestion(self.wordList)

	def test_true_question(self):
		self.assertTrue(self.question.isCorrect('8'))
		self.assertTrue(self.question.isCorrect('8 '))

	def test_true_generated_question(self):
		self.assertTrue(self.generatedQuestion.isCorrect(self.generatedQuestion.answer))
		
	def test_false_question(self):
		self.assertFalse(self.question.isCorrect('Kalle Anka'))
		self.assertFalse(self.question.isCorrect('9'))

if __name__  =='__main__':
	unittest.main()
