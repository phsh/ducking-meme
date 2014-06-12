#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import random, array
from random import shuffle
from random import randint
from random import choice
from Question import Question

seperator = "=========" * 10

print seperator
print "Frågesport"
print seperator

aLotOfQuestions = {
	" 2 +  6 ? ": "8", " 4 +  6 ? ": "10",
	" 4 +  8 ? ": "12"," 1 + 13 ? ": "14",
	" s ä t H ? ": "Häst", " r s i G ? ": "Gris",
	" 2 +  5 ? ": "7", " R s o ? ": "Ros",
	" o B k ? ": "Bok", " S o k ? ": "Sko",
	" F s i k ? ": "Fisk", " 4 + 5 ?": "9",
	" t å B ? ": "Båt"
}

level_one = [
'Fisk','Ros','Sko',
'Gris', 'Stol', 'Hus', 
'Mus', 'Hund', 'Katt',
'Hand'
]

def generateMathQuestion(start_base, end_base ):
	value_a = randint(start_base , end_base)
	value_b = randint(start_base , end_base)
	question = " " + str(value_a) + " + " + str(value_b) + " ? "
	answer = str(value_a+value_b)
	return Question(question,answer)

def generateWordQuestion(list_of_words=level_one):
	answer = choice(list_of_words)
	word = list(answer)
	shuffle(word)
	result = " ".join(word)
	question = result + " ? " 
	return Question(question, answer)

questions = list()

for x in xrange(0,5):
	questions.append(generateWordQuestion())
	questions.append(generateMathQuestion(1,10))

'''
questionsFile = open("questions.csv","w")
w = csv.writer(questionsFile)
for key, val in aLotOfQuestions.items():
	w.writerow([key,val])
	questions.append(Question(key,val))
questionsFile.close()
'''

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
elif len(questions)-antal_correct <=3:
	print "SILVERSTJÄRNA!!!"
	print seperator