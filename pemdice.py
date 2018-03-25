
from math import sqrt

# list of shape groups
AS, NEG, MD, RT, MID, LF, JUX, PAR, CON, INT, FRA = range(11)

Arity = [2, 1, 2, 1, 2, 1, 2, 1, 2, 0]

DICE = {
	'+': AS, '-': AS,
	'*': MD, '/': MD,
	'^2': RT, '^3': RT, '!': RT, '**2': RT, '**3': RT,
	'^': MID, '**': MID,
	'sqrt': LF, 'cbrt': RT,
	'1/2': FRA, '1/3': FRA, '1/4': FRA,
}
for i in '2,3,4,5,6,7,8,9,10,20,30,40,50,60,100'.split(','):
	DICE[i] = INT

def S(tup):
	if tup is INT: return '3'
	op, rest = tup[0], tup[1:]
	if op is AS: 	return S(rest[0]) + '+' + S(rest[1])
	if op is NEG: 	return '-' + S(rest[0])
	if op is MD: 	return S(rest[0]) + '*' + S(rest[1])
	if op is RT: 	return S(rest[0]) + '**2'
	if op is MID:	return S(rest[0]) + '**' + S(rest[1])
	if op is LF: 	return 'sqrt(' + S(rest[0]) + ')'
	if op is JUX: 	return S(rest[0]) + S(rest[1])
	if op is PAR: 	return '(' + S(rest[0]) + ')'
	if op is CON: 	return S(rest[0]) + S(rest[1])
	# if op is INT: return '?'

# def parseDice(dice):
# 	return map(lambda x: (DICE[x], x), dice.split(', '))


t = (AS, (MD, (PAR, (AS, INT, (LF, (CON, INT, INT)))), (NEG, INT)), (RT, INT))
print(S(t))
print(eval(S(t)))

dice = "2, 3, /, 1/3, 8, *, cbrt, +, ^3, -, 3, 30".split(', ')
print(dice.count('-') > dice.count('^'))





def halve(L): return [L[0]//2]+L[1:] if L[0] else [0]+halve(L[1:])


