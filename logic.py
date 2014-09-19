# -*- encoding: utf-8 -*-

import itertools

def analyze(formula, symbols):
  formula.replace(" ", "")
  for m in itertools.product([0, 1], repeat=len(symbols)):
    mappings = {s: i for s, i in zip(symbols, m)}
    print(mappings)
    print(evaluate(formula, mappings)[0])

def compare(f1, f2, symbols):
  f1.replace(" ", "")
  f2.replace(" ", "")
  for m in itertools.product([0, 1], repeat=len(symbols)):
    mappings = {s: i for s, i in zip(symbols, m)}
    print(mappings)
    e1 = evaluate(f1, mappings)[0]
    e2 = evaluate(f2, mappings)[0]
    if (e1 != e2):
      print f1.encode("utf-8"), e1
      print f2.encode("utf-8"), e2
    else:
      print(e1)
  
def And(x, y):
  return x and y
  
def Or(x, y):
  return x or y
  
def Implies(x, y):
  return y or (1 - x)

def Iff(x, y):
  return x == y

f = {u"∧": And, u"∨": Or, u"⊃": Implies, u"⇔": Iff}

def evaluate(formula, mappings):
  if (formula[0] == "("):
    arg1, formula = evaluate(formula[1:], mappings)
    op = formula[0]
    arg2, formula = evaluate(formula[1:], mappings)
    # print op.encode("utf-8")
    return f[op](arg1, arg2), formula[1:]
  if (formula[0] in mappings):
    return mappings[formula[0]], formula[1:]
  if (formula[0] == u"¬"):
    exp = evaluate(formula[1:], mappings)
    return 1 - exp[0], exp[1]

compare(u"((P∧¬Q)⇔P)", u"(¬P∨¬Q)", ["P", "Q"])
   
