import numpy as np
from jmetal.core.problem import IntegerProblem
from jmetal.core.solution import IntegerSolution

from testing import calculate_fail_number_GA


class TestingProblem(IntegerProblem):
    def __init__(self, number_of_variables, dec2bin_param, group_name, program_name, algorithm):
        super(IntegerProblem).__init__()
        self.number_of_variables = number_of_variables
        self.number_of_objectives = 1
        self.number_of_constraints = 0

        # self.obj_directions = [self.MAXIMIZE]
        self.obj_directions = [self.MINIMIZE]
        self.lower_bound = self.number_of_variables * [0]

        if number_of_variables == 50:
            self.upper_bound = self.number_of_variables * [1023]
        elif number_of_variables == 7:
            self.upper_bound = self.number_of_variables * [127]
        elif number_of_variables == 26:
            self.upper_bound = self.number_of_variables * [511]
        else:
            self.upper_bound = self.number_of_variables * [-1]

        self.dec2bin_param = dec2bin_param
        self.group_name = group_name

        self.program_name = program_name
        self.algorithm = algorithm

    def evaluate(self, solution: IntegerSolution) -> IntegerSolution:
        variables = np.array(solution.variables)
        p = calculate_fail_number_GA(variables, self.dec2bin_param, self.group_name, self.program_name, self.algorithm)
        # the value is negated because we want to maximize "p" using a minimization problem
        solution.objectives[0] = -p
        return solution

    def get_name(self) -> str:
        return 'TestingProblem'
