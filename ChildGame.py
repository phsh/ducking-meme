#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv, os
import random, array
from random import shuffle
from random import randint
from random import choice
from Question import Question

seperator = "=========" * 10

zero = [
'Bi', 'Lo', 'Nu',
'Ut', 'Om', 'En',
'Yr', 'Ek', 'Se',
'Sy', 'Av', 'Du'
]

one = [
'Bil', 'Bok', 'Vas',
'Ros', 'Sko', 'Hus',
'Yxa', 'Lax', 'Mus',
'Ord', 'Oxe', 'Arg'
]

two = [
'Fisk','Gris', 'Stol',  
'Hund', 'Katt','Hand', 
'Saga', 'Film', 'Jobb',
'Sten', 'Gren'
]

three = [
'Matta', 'Pappa', 'Mamma',
'Torsk', 'Potatis', 'Fluga',
'Tunnel', 'Farmor', 'Farfar',
'Mormor', 'Morfar', 'Gammal',
'Groda', 'Flygplan','Pannkaka'
]

level_word = [zero, one, two, three]
level_math = [ 1, 5, 10, 15]
GOLD=0
SILVER=1
MAX_LEVEL = 4
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
os.system('clear')
print seperator
print "Frågesport "
print seperator
antal_fragor_total = 0;
antal_correct_total = 0;
stars = [ 0, 0 ]
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
		stars[GOLD] += 1		
		print seperator
		print seperator
	elif len(questions)-antal_correct <=3:
		print "SILVERSTJÄRNA!!!"
		stars[SILVER] += 1		
		print seperator
		print seperator
print seperator
print "Du hade %s rätt utav %s frågor totalt" % (antal_correct_total, antal_fragor_total)
print "Du hade %s GULDSTJÄRNOR och %s SILVERSTJÄRNOR" % (stars[GOLD],stars[SILVER])
print seperator
