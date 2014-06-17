#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv, os
import random, array

from Question import Question
from QuestionGenerator import QuestionGenerator
from Level import Level

seperator = "=========" * 10



GOLD=0
SILVER=1

NUMBER_OF_QUESTIONS = 5

os.system('clear')
print seperator
print "Frågesport "
print seperator
antal_fragor_total = 0;
antal_correct_total = 0;
stars = [ 0, 0 ]
for level in range(Level.MAX_LEVEL):
	print "LEVEL " + str(level + 1)
	print seperator
	questions = list()

	for x in range(NUMBER_OF_QUESTIONS):
		questions.append(QuestionGenerator.generateWordQuestion(Level.level_word[level]))
		questions.append(QuestionGenerator.generateMathQuestion(Level.level_math[level],Level.level_math[level]+5))
	random.shuffle(questions)
	antal_correct = 0
	for question in questions:
		answer = raw_input(question.question + " :")
		antal_fragor_total += 1
		if question.isCorrect(answer):
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
