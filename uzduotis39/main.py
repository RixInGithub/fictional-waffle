# math
import random

# pick number when nest > parens or 50% fails
# pick number when no nest or 50% succeeds

def genExpr(nest=0):
	r = random.randint(0,1)
	if nest > parens or (r==1 and nest > 0): return random.randint(1,10)
	return {"lhs":genExpr(nest+1),"rhs":genExpr(nest+1),"op":random.choice("+-*/")}

def stringify(exp, nested=False):
	if type(exp)==int: return str(exp)
	return f"{'(' if nested else ''}{stringify(exp['lhs'], True)} {exp['op']} {stringify(exp['rhs'], True)}{')' if nested else ''}"

def parse(exp):
	if type(exp)==int: return exp
	a = parse(exp["lhs"])
	b = parse(exp["rhs"])
	op = exp["op"]
	if op == "+": return a + b
	if op == "-": return a - b
	if op == "*": return a * b
	if op == "/": return a / b

n = 5
count = 0
parens = 1
ok = 0
while count < n:
	exp = genExpr()
	ans = float(parse(exp))
	usr = 0
	try:
		usr = float(input(stringify(exp)+" = "))
	except: pass
	ok += usr==ans
	count += 1

print("/".join([str(ok),str(n)])+",", round((ok * 10) / n))