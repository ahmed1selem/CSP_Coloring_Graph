import random
import matplotlib.pyplot as plt
import geopandas
class Problem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints 

    def solve(self):
        assignments = {}  
        self.backtrack(assignments)
        self.map_plot(assignments)
        return assignments

    def backtrack(self, assignments):
        self.map_plot(assignments)
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
    def map_plot(self,soulation):
        print("Ready to plot map for AUS")
        path = "./aus_basic/"
        # # load the shape file using geopandas
        states = geopandas.read_file(path + 'STE_2016_AUST.shp')
        states = states.to_crs("EPSG:3395")
        print(states)
        ax2 = states.boundary.plot(figsize=(12, 12), edgecolor=u'gray')
        print(soulation)
        if soulation is not None:
            for k, v in soulation.items():
                print(k)
                print( states[states.STE_NAME16 == k])
                if v == 'R':
                    states[states.STE_NAME16 == k].plot(edgecolor=u'gray', color='yellow', ax=ax2)
                elif v == 'B':
                    states[states.STE_NAME16 == k].plot(edgecolor=u'gray', color='blue', ax=ax2)
                elif v == 'G':
                    states[states.STE_NAME16 == k].plot(edgecolor=u'gray', color='green', ax=ax2)
                else:
                    states[states.STE_NAME16 == k].plot(edgecolor=u'gray', color='red', ax=ax2)

            plt.show()


# Define the problem
# Define the variables (regions) and their possible values (colors)
#MAP:::https://www.worldmap1.com/map-australia.asp
variables = ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales', 'Victoria', 'Tasmania']
  # Australia Regions
domains = ['R', 'G', 'B',"R"]
constraints = [
    ('Western Australia', 'Northern Territory'),
    ('Western Australia', 'South Australia'),
    ('Northern Territory', 'South Australia'),
    ('Northern Territory', 'Queensland'),
    ('South Australia', 'Queensland'),
    ('South Australia', 'New South Wales'),
    ('South Australia', 'Victoria'),
    ('New South Wales', 'Queensland'),
    ('New South Wales', 'Victoria'),
    ('Tasmania','Victoria')
]

problem = Problem(variables, domains, constraints)
#
# Solve the problem
solution = problem.solve()
print(solution)


# states = geopandas.read_file("./canda_map/canda_map.shp")
# states = states.to_crs("EPSG:3395")
# print("sdfsfd",states)
