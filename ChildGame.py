#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv, os
import random, array
import time
from Question import Question
from QuestionGenerator import QuestionGenerator
from Level import Level

def generateQuestions(level):
	questions = list()

	for x in range(NUMBER_OF_QUESTIONS):
		questions.append(QuestionGenerator.generateWordQuestion(Level.level_word[level]))
		questions.append(QuestionGenerator.generateMathQuestion(Level.level_math[level],Level.level_math[level]+5))
	random.shuffle(questions)
	return questions


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

def startLevel(level):
	print "LEVEL %s" % (level + 1)
	print seperator
	questions = generateQuestions(level)
	return questions
start = time.time()
for level in range(Level.MAX_LEVEL):
	antal_correct_level = 0
	questions = startLevel(level)
	for question in questions:
		answer = raw_input(question.question + " :")
		antal_fragor_total += 1
		if question.isCorrect(answer):
			antal_correct_level += 1
			antal_correct_total += 1
			print "Rätt"
		else:
			print "Fel, rätt svar " + question.answer 

	print seperator
	print "Du hade %s rätt utav %s frågor i denna level" % (antal_correct_level, len(questions))
	print seperator
	if len(questions)-antal_correct_level <= 1:
		print "GULDSTJÄRNA!!!"
		stars[GOLD] += 1		
		print seperator		
	elif len(questions)-antal_correct_level <=3:
		print "SILVERSTJÄRNA!!!"
		stars[SILVER] += 1		
		print seperator		

print seperator
print "Du hade %s rätt utav %s frågor totalt" % (antal_correct_total, antal_fragor_total)
print "Du hade %s GULDSTJÄRNOR och %s SILVERSTJÄRNOR" % (stars[GOLD],stars[SILVER])
print "Det tog %.3f sekunder." % ( time.time() - start )
print seperator



