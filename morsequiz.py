import os, sys
from random import randint

morse={	
	"A":". _",
	"B":"_ ...",
	"C":"_ . _ .",
	"D":"_ ..",
	"E": ".",
	"F": ".. _ .",
	"G": "_ _ .",
	"H": "....",
	"I": "..",
	"J": ". _ _ _",
	"K": "_ . _",
	"L": ". _ ..",
	"M": "_ _",
	"N": "_ .",
	"O": "_ _ _",
	"P": ". _ _ .",
	"Q": "_ _ . _",
	"R": ". _ .",
	"S": "...",
	"T": "_",
	"U": ".. _",
	"V": "... _",
	"W": ". _ _",
	"X": "_ .. _",
	"Y": "_ . _ _",
	"Z": "_ _ ..",
}

questions=15
rightAnswers=0
for x in range(questions):
	key=morse.keys()[randint(0,len(morse)-1)]
	answer=raw_input("What is the letter for "+morse[key]+"? ")
	if answer.upper()==key:
		del morse[key]
		print("Right answer!")
		rightAnswers+=1
	else:
		print("Wrong, the answer is "+key)

print("You have "+str(rightAnswers)+" right answers out of "+str(questions)+".")