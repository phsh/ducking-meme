#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
from Question import Question

seperator = "=========" * 10

print seperator
print "Frågesport"
print seperator

aLotOfQuestions = {
	" 2 +  6 ? ": "8", " 4 +  6 ? ": "10",
	" 4 +  8 ? ": "12"," 1 + 13 ? ": "14",
	" s ä t H ?": "Häst", " r s i G ?": "Gris",
	" 2 +  5 ?": "7", " R s o ?": "Ros",
	" o B k ?": "Bok"
}

questions = list()
questionsFile = open("questions.csv","w")
w = csv.writer(questionsFile)
for key, val in aLotOfQuestions.items():
	w.writerow([key,val])
	questions.append(Question(key,val))
questionsFile.close()


antal_correct = 0
for question in questions:
	answer = raw_input(question.question + " :")
	if answer.lower().strip() == question.answer.lower().strip():
		antal_correct += 1
		print "Rätt"
	else:
		print "Fel"

print seperator
print "Du hade %s rätt utav %s frågor" % (antal_correct, len(questions))
print seperator
if len(questions)-antal_correct <= 1:
	print "GULDSTJÄRNA!!!"
	print seperator
elif len(questions)-antal_correct <=3:
	print "SILVERSTJÄRNA!!!"
	print seperator