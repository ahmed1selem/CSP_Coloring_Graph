from solver import *

# Define the problem
# Define the variables (regions) and their possible values (colors)
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V',"T"]  # Australia Regions
domains = ['r', 'g', 'b']
constraints = [
    ('WA', 'NT'),
    ('WA', 'SA'),
    ('NT', 'SA'),
    ('NT', 'Q'),
    ('SA', 'Q'),
    ('SA', 'NSW'),
    ('SA', 'V'),
    ('NSW', 'Q'),
    ('NSW', 'V'),
    ("T","V")
]

problem = Problem(variables, domains, constraints)

# Solve the problem
solution = problem.solve()
print(solution)
