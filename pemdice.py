
from math import sqrt
# from copy import copy, deepcopy

# list of shape groups
# EQ, AS, NEG, MD, RT, MID, LF, JUX, PAR, CON, INT, FRA = range(12)

# Arity = [2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0, 0]

# LE, EQ, GE = -1, 0, 1

# LIMS = [
# 	[(GE, EQ), (GE, EQ)],
# 	[(GE, AS), (GE, MD)],
# 	[(GE, MD)],
# 	[(GE, MD), (GE, RT)],
# 	[(GE, RT)],
# 	[(GE, MID), (GE, LF)],
# 	[(GE, LF)],
# 	[(GE, PAR), (EQ, PAR)],
# 	[PAR], ## more than in
# 	[(EQ, INT), (GE, PAR)],
# 	[],
# 	[]
# ]


numOps = 11
AS, NEG, MD, RT, MID, LF, NUM,    EQ, JUX, INT, FRA = range(numOps)

Arity = [2, 1, 2, 1, 2, 1, 0]

LE, EQ, GE = -1, 0, 1

LIMS = [
	[(GE, AS), (GE, MD)],
	[(GE, MD)],
	[(GE, MD), (GE, RT)],
	[(GE, RT)],
	[(GE, MID), (GE, LF)],
	[(GE, LF)],
	[]
]



DICE = {
	'-': NEG,
	'+': AS, #'-': AS,
	'*': MD, '/': MD,
	'^2': RT, '^3': RT, '!': RT, #'**2': RT, '**3': RT,
	'^': MID, #'**': MID,
	'sqrt': LF, 'cbrt': LF,
	'1/2': FRA, '1/3': FRA, '1/4': FRA,
}
for i in '2,3,4,5,6,7,8,9,10,20,30,40,50,60,100'.split(','):
	DICE[i] = INT

def S(tup):
	if tup is NUM: return '3'
	op, rest = tup[0], tup[1:]
	if op is AS: 	return S(rest[0]) + '+' + S(rest[1])
	if op is NEG: 	return '-' + S(rest[0])
	if op is MD: 	return S(rest[0]) + '*' + S(rest[1])
	if op is RT: 	return S(rest[0]) + '**2'
	if op is MID:	return S(rest[0]) + '**' + S(rest[1])
	if op is LF: 	return 'sqrt(' + S(rest[0]) + ')'
	if op is JUX: 	return S(rest[0]) + S(rest[1])
	if op is PAR: 	return '(' + S(rest[0]) + ')'
	# if op is CON: 	return S(rest[0]) + S(rest[1])
	# if op is INT: return '?'

def test(C): return C[INT]+C[FRA]-C[CON]-C[JUX] == C[AS]+C[MD]+C[EQ]+1

# def parseDice(dice):
# 	return map(lambda x: (DICE[x], x), dice.split(', '))


# t = (AS, (MD, (PAR, (AS, INT, (LF, (CON, INT, INT)))), (NEG, INT)), (RT, INT))
# print(S(t))
# print(eval(S(t)))

# dice = "2 3 / 1/3 8 * cbrt - ^ - 3 30".split()
dice = "20 - 2 ^2 1/2 - * 5 9 5 + ^2".split()
# dice = "4 10 8 3 2 + * *".split()
COUNTS = [0 for _ in range(numOps)]
for d in dice: COUNTS[DICE[d]] += 1
# COUNTS[PAR] = 1
# COUNTS[EQ] = 1
ints = list(filter(lambda d: DICE[d] is INT, dice))
fra = list(filter(lambda d: DICE[d] is FRA, dice))[0]
print(ints)
print(fra)

# hardcoded sets of numbers based on number of concats available:
numSets = [[ints+[fra]], [], []]
print(numSets)

negsAndSubs = COUNTS[NEG]
exps = COUNTS[MID]
diff = negsAndSubs-exps
for negs in range(diff+1):
	subs = negsAndSubs - negs
	consAndJuxes = negs
	for juxes in range(min(consAndJuxes+1, 2)):
		cons = consAndJuxes - juxes
		print(negs, subs, exps, cons, juxes)
		# counts = list(COUNTS)
		# counts[NEG] = negs
		# counts[AS] += subs
		# counts[CON] = cons
		# counts[JUX] = juxes
		# print(counts)
		# print(test(counts))
		



def halve(L): return [L[0]//2]+L[1:] if L[0] else [0]+halve(L[1:])


