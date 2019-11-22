from z3 import *
solver=Solver()
p=Bool('p')
q=Bool('q')
r=Bool('r')
solver.add(Not(Implies(And(Implies(p,q),Implies(q,r)),Implies(p,r))))
solver.check()
