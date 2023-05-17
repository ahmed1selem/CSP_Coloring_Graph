import random 
class Problem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints 

    def solve(self):
        assignments = {}  
        self.backtrack(assignments)
        return assignments

    def backtrack(self, assignments):
        if len(assignments) >= len(self.variables):##>=
            return True

        variable = self.select_unassigned_variable(assignments)  # 1.select Unassigned Var

        for value in self.domains:
            if self.is_consistent(variable, value, assignments):#2. select  value (Red->Green->Blue) and check it 
                 assignments[variable] = value
                 if self.backtrack(assignments):
                    return True
        return False

    def select_unassigned_variable(self, assignments):
        unassigned_variables=[] #NOTE append to unassignedList and select Randomly
        for variable in self.variables:
            if variable not in assignments:
                unassigned_variables.append(variable)
        randomNumber=random.randint(0,len(unassigned_variables)-1)#inclusive
        return unassigned_variables[randomNumber]
        

    def is_satisfied(self, constraint, assignments):  # given constrains in pairs should never be equal
        if (constraint[0] in assignments) and (constraint[1] in assignments):
            return assignments[constraint[0]] != assignments[constraint[1]]
        return True

    def is_consistent(self, variable, value, assignments):
        assignments[variable] = value#3. try assign selected var to selected value
        for constraint in self.constraints:#4. check all avialable constriants 
            if  not self.is_satisfied(constraint, assignments):
                del assignments[variable]#5. if any Constraint is broke
                return False
        return True#6. if all constraints are well !




# Define the problem
# Define the variables (regions) and their possible values (colors)
#MAP:::https://www.worldmap1.com/map-australia.asp
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V','T']  # Australia Regions
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
    ('T','V')
]

problem = Problem(variables, domains, constraints)

# Solve the problem
solution = problem.solve()
print(solution)