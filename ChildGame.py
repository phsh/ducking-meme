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
level = 0

def generateMathQuestion(start_base=level_math[level], end_base = level_math[level]+5):
	value_a = randint(start_base , end_base)
	value_b = randint(start_base , end_base)
	question = " %s + %s ? " % (value_a, value_b)
	answer = str(value_a+value_b)
	return Question(question,answer)

def generateWordQuestion(list_of_words=level_word[level]):
	answer = choice(list_of_words)
	word = list(answer)
	shuffle(word)
	result = " ".join(word)
	question = " " + result + " ? " 
	return Question(question, answer)



print seperator
print "Frågesport "
print seperator

questions = list()

for x in xrange(0,5):
	questions.append(generateWordQuestion())
	questions.append(generateMathQuestion())

antal_correct = 0
for question in questions:
	answer = raw_input(question.question + " :")
	if answer.lower().strip() == question.answer.lower().strip():
		antal_correct += 1
		print "Rätt"
	else:
		print "Fel, rätt svar " + question.answer 

print seperator
print "Du hade %s rätt utav %s frågor" % (antal_correct, len(questions))
print seperator
if len(questions)-antal_correct <= 1:
	print "GULDSTJÄRNA!!!"
	print seperator
	print seperator
elif len(questions)-antal_correct <=3:
	print "SILVERSTJÄRNA!!!"
	print seperator
	print seperator
