"""
Boolean expression generator simple to complicated

- eval
- ast module
- sympy logic module
- pyparsing
- lex/yacc
- llvm
- build lexer/parser by hand
cf pypy rpython


eval and ast module -> boolean evaluator (is|can easily be turned into) valid python
sympy -> has tools for this specific task
pyparsing -> seems good compromise between ease of use and moderately copmlicated grammars
lex/yacc -> overkill
"""

from sympy import symbols, true

dict1 = {'((A or D or E) AND F) AND NOT G': 'Pickles', '(A AND B) OR E': 'Tuna'}
dict2 = {'A': 'Accepted', 'B': 'Rejected', 'C': 'Rejected', 'D': 'Accepted', 'E': 'Rejected', 'F': 'Accepted', 'G': 'Rejected'}

mapping_operators = {'AND': '&', 'OR': '|' , 'NOT': '~'}
mapping_values = {'Accepted': True, 'Rejected': False}

A,B,C,D,E,F,G = symbols('A,B,C,D,E,F,G')

class ParseError:
    pass

try:
    values = {k:mapping_values[v] for k,v in dict2.items()}
except KeyError as e:
    raise ParseError
    
def convert_expr(expr):
    for k,v in mapping_operators.items():
        expr = expr.replace(k, v)
    return expr
    
results = []    
for k in dict1:
    mapped = convert_expr(k)
    sp_expr = eval(mapped)
    res = sp_expr.subs(values)
    # sympy.true is not Python's True
    if res == true:
        results.append(dict1[k])
        
print(results)



