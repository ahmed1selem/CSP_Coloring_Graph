from solver import *

# Define the problem
# Define the variables (regions) and their possible values (colors)
mapChoice =input("Choose map: \n1. Australia \n2. USA")
if mapChoice=="Australia":
    variables = ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales',
                 'Victoria', 'Tasmania']
    # Australia Regions
    domains = ['R', 'G', 'B', "Y"]
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
        ('Tasmania', 'Victoria')
    ]
else:
    variables=[
        'Alberta',
        'British Columbia',
        'Manitoba',
        'New Brunswick',
        'Newfoundland and Labrador',
        'Northwest Territories',
        'Nova Scotia',
        'Nunavut',
        'Ontario',
        'Prince Edward Island',
        'Quebec',
        'Saskatchewan',
        'Yukon'
    ]
    constraints = [
        ('Alberta', 'British Columbia'),
        ('Alberta', 'Northwest Territories', 'Saskatchewan'),
        ('Alberta', 'Mississippi'),
        ('Alberta', 'Saskatchewan'),
        ('British Columbia', 'Yukon'),
        ('British Columbia', 'Northwest Territories'),
        ('New Brunswick', 'Quebec'),
        ('New Brunswick', 'Prince Edward Island'),
        ('New Brunswick', 'Nova Scotia'),
        ('Manitoba', 'Saskatchewan'),
        ('Manitoba', 'Ontario'),
        ('Manitoba', 'Northwest Territories'),
        ('Manitoba', 'Nunavut'),
        ('Manitoba', 'Utah'),
        ('Northern Territory', 'Queensland'),
        ('South Australia', 'Queensland'),
        ('South Australia', 'New South Wales'),
        ('South Australia', 'Victoria'),
        ('New South Wales', 'Queensland'),
        ('New South Wales', 'Victoria'),
        ('Tasmania', 'Victoria')
    ]
problem = Problem(variables, domains, constraints)

# Solve the problem
solution = problem.solve()
print(solution)
