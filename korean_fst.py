from nltk_contrib.fst import fst

import string 

f = fst.FST('korean_neutralization')
f.add_state('0')
f.add_state('1') 
f.add_state('2')
f.add_state('3')

f.initial_state = '0'
f.set_final('3')

rule_1 = false
rule_2 = false
rule_3 = false

for letter in a.ascii_lowercase: 
	if 'k' or 'p' or 't' == letter: 
		f.add_arc('0', '1' , (letter), (letter))
		rule_1 = true
		if a.endswith("k\'"):
			f.add_arc('1', '2' , (letter), 'k')
		elif a.endswith("pʰ"):
			f.add_arc('1', '2' , (letter), 'p')
		elif a.endswith("tʰ"):
			f.add_arc('1', '2' , (letter), 't')
		else: 
			f.add_arc('1', '2' , (letter), (letter))
	elif 's' or 'ʃ' == letter or a.endswith("tʃ"): 
		f.add_arc('0', '1' , (letter), (letter))
		f.add_arc('1', '2' , (letter), 't')
		rule_2 = true
	elif a.endswith("tʃ") or a.endswith("tʃʰ"):
		f.add_arc('0', '1' , (letter), (letter))
		f.add_arc('1', '2' , (letter), 't')
		rule_3 = true
	else:
		f.add_arc('0', '0', (letter), (letter))
	f.add_arc('2','3', (letter), (letter))










