!pip install ortools

from ortools.linear_solver import pywraplp

# Solver erstellen (SCIP ist Open-Source)
solver = pywraplp.Solver.CreateSolver('SCIP')

# Variablen definieren
x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')

# Nebenbedingungen hinzufügen
solver.Add(x + 2*y <= 14)
solver.Add(3*x - y >= 0)
solver.Add(x - y <= 2)

# Zielfunktion definieren
solver.Maximize(3*x + 4*y)

# Problem lösen
status = solver.Solve()

# Ergebnis ausgeben
if status == pywraplp.Solver.OPTIMAL:
    print(f'Optimale Lösung gefunden:')
    print(f'x = {x.solution_value()}')
    print(f'y = {y.solution_value()}')
    print(f'Maximaler Wert der Zielfunktion: {solver.Objective().Value()}')
else:
    print('Keine optimale Lösung gefunden!')
