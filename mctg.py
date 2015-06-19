#!/usr/bin/python
# Markov Chain Text Generator
import sys
import random

chain = {}
tok = '.'
outputLength = 100
if len(sys.argv) >= 2:
	outputLength = int(sys.argv[1])
	
for line in sys.stdin:
	l = line.split()
	for ss in l:
		if ss.endswith(',') or ss.endswith('.'):
			s = ss[:-1].lower()
		else:
			s = ss.lower()
		if tok in chain:
			if s in chain[tok]:
				chain[tok][s] += 1
			else:
				chain[tok][s] = 1
		else:
			chain[tok]={s:1}
		tok = s
		if ss.endswith(',') or ss.endswith('.'):
			if tok in chain:
				if ss[-1] in chain[tok]:
					chain[tok][ss[-1]] += 1
				else:
					chain[tok][ss[-1]] = 1
			else:
				chain[tok]={ss[-1]:1}
			tok = ss[-1]
		
#print outputLength
#print chain		
dist = {}
for key in chain:
	dist[key] = 0
	for s in chain[key]:
		dist[key] += chain[key][s]

prev = '.' #start new sentence

for i in range(outputLength):
	n = int( random.random() * dist[prev])
	j = 0
	for k in chain[prev]:
		j += chain[prev][k]
		if j > n:
			next = k
			break
	#next = chain[prev].keys()[n]
	if prev=='.':
		sys.stdout.write(' '+next[0].upper() + next[1:])
	elif next in [',','.']:
		sys.stdout.write(next)
	else:
		sys.stdout.write(' ' + next)
	prev = next
	
