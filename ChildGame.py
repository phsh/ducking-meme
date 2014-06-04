#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Question:
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

questions = [ 
Question("Vad är 2 + 6 ?","8"), 
Question("Vad är 4 + 6 ?","10"), 
Question("Vad är 4 + 8 ?","12"), 
Question("Vad är 1 + 13 ?","14") 
]
antal_correct = 0
for question in questions:
	answer = raw_input(question.question + " :")
	if answer == question.answer:
		antal_correct += 1
		print "Rätt"
	else:
		print "Fel"

print "------------------"
print "Du hade %s rätt utav %s frågor" % (antal_correct, len(questions))
print "------------------"


