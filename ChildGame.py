#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import random, array
from random import shuffle
from random import randint
from random import choice
from Question import Question

seperator = "=========" * 10

zero = [
'Bi', 'Lo', 'Nu',
'Ut', 'Om', 'En',
'Yr' 
]

one = [
'Fisk','Ros','Sko',
'Gris', 'Stol', 'Hus', 
'Mus', 'Hund', 'Katt',
'Hand', 'Lax', 'Yxa',
'Saga', 'Film', 'Bil',
'Sten', 'Gren'
]

two = [
'Matta', 'Pappa', 'Mamma',
'Torsk', 'Potatis', 'Fluga',
'Tunnel', 'Farmor', 'Farfar',
'Mormor', 'Morfar', 'Gammal',
'Groda'
]

level_word = [zero, one, two]
level_math = [ 1, 5, 10]

MAX_LEVEL = 3
NUMBER_OF_QUESTIONS = 5
def generateMathQuestion(start_base=level_math[0], end_base = level_math[0]+5):
	value_a = randint(start_base , end_base)
	value_b = randint(start_base , end_base)
	question = " %s + %s ? " % (value_a, value_b)
	answer = str(value_a+value_b)
	return Question(question,answer)

def generateWordQuestion(list_of_words=level_word[0]):
	answer = choice(list_of_words)
	word = list(answer)
	shuffle(word)
	result = " ".join(word)
	question = " " + result + " ? " 
	return Question(question, answer)

print seperator
print "Frågesport "
print seperator
antal_fragor_total = 0;
antal_correct_total = 0;
antal_gold_stars = 0;
antal_silver_stars = 0;
for level in range(MAX_LEVEL):
	print "LEVEL " + str(level + 1)
	print seperator
	questions = list()

	for x in range(NUMBER_OF_QUESTIONS):
		questions.append(generateWordQuestion(level_word[level]))
		questions.append(generateMathQuestion(level_math[level],level_math[level]+5))
	shuffle(questions)
	antal_correct = 0
	for question in questions:
		answer = raw_input(question.question + " :")
		antal_fragor_total += 1
		if answer.lower().strip() == question.answer.lower().strip():
			antal_correct += 1
			antal_correct_total += 1
			print "Rätt"
		else:
			print "Fel, rätt svar " + question.answer 

	print seperator
	print "Du hade %s rätt utav %s frågor i denna level" % (antal_correct, len(questions))
	print seperator
	if len(questions)-antal_correct <= 1:
		print "GULDSTJÄRNA!!!"
		antal_gold_stars +=1
		print seperator
		print seperator
	elif len(questions)-antal_correct <=3:
		print "SILVERSTJÄRNA!!!"
		antal_silver_stars +=1
		print seperator
		print seperator
print seperator
print "Du hade %s rätt utav %s frågor totalt" % (antal_correct_total, antal_fragor_total)
print "Du hade %s GULDSTJÄRNOR och %s SILVERSTJÄRNOR" % (antal_gold_stars,antal_silver_stars)