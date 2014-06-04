#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv

class Question:
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

questions = [ 
Question(" 2 +  6 ? ", "8"), 
Question(" 4 +  6 ? ", "10"), 
Question(" 4 +  8 ? ", "12"), 
Question(" 1 + 13 ? ", "14"),
Question(" s ä t H ?", "Häst"),
Question(" r s i G ?", "Gris"),
Question(" 2 +  5 ?", "7"),
Question(" R s o ?", "Ros"),
Question(" o B k ?", "Bok")
]

aLotOfQuestions = {
	" 2 +  6 ? ": "8", " 4 +  6 ? ": "10",
	" 4 +  8 ? ": "10"," 1 + 13 ? ": "14",
	" s ä t H ?": "Häst", " r s i G ?": "Gris"
}

w = csv.writer(open("questions.csv","w"))
for key, val in aLotOfQuestions.items():
	w.writerow([key,val])



antal_correct = 0
for question in questions:
	answer = raw_input(question.question + " :")
	if answer.lower() == question.answer.lower():
		antal_correct += 1
		print "Rätt"
	else:
		print "Fel"

print "------------------"
print "Du hade %s rätt utav %s frågor" % (antal_correct, len(questions))
print "------------------"


