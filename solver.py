class Problem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints  # how list ?



    def solve(self):
        assignments = {}  # can't be represented by nCr,must be given
        self.backtrack(assignments)
        return assignments

    def backtrack(self, assignments):
        if len(assignments) >= len(self.variables):
            return True

        variable = self.select_unassigned_variable(assignments)  # find the unassigned var

        for value in self.domains:
            if self.is_consistent(variable, value, assignments):
                assignments[variable] = value
                if self.backtrack(assignments):
                    return True
                else:
                    del assignments[variable]
        return False

    def select_unassigned_variable(self, assignments):
        for variable in self.variables:
            if variable not in assignments:
                return variable

    def is_satisfied(self, constraint, assignments):  # given constrains in pairs should never be equal
        if (constraint[0] in assignments) and (constraint[1] in assignments):
            return assignments[constraint[0]] != assignments[constraint[1]]
        return True

    def is_consistent(self, variable, value, assignments):
        assignments[variable] = value
        for constraint in self.constraints:
            if not self.is_satisfied(constraint, assignments):
                del assignments[variable]
                return False
        #del assignments[variable]
        return True
