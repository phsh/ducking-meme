# _author
from random import shuffle
from random import randint
from random import choice
from Question import Question

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