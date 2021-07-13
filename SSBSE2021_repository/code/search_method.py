import os

import numpy as np
from jmetal.algorithm.multiobjective import RandomSearch
from jmetal.algorithm.singleobjective import GeneticAlgorithm
from jmetal.operator import IntegerPolynomialMutation
from jmetal.operator import IntegerSBXCrossover
from jmetal.operator.selection import BestSolutionSelection
from jmetal.util.termination_criterion import StoppingByEvaluations

from TestingProblem import TestingProblem


class Search:

    @staticmethod
    def search(dec2bin_param, group_name, program_name, alg):
        folder = './result/' + group_name
        if not os.path.exists(folder):
            os.makedirs(folder)
        num_vars = -1
        if dec2bin_param == 10:
            num_vars = 50
        elif dec2bin_param == 11:
            num_vars = 50
        elif dec2bin_param == 7:
            num_vars = 7
        elif dec2bin_param == 4:
            num_vars = 26
        else:
            num_vars = -1
        problem = TestingProblem(num_vars, dec2bin_param, group_name, program_name, alg)
        np.set_printoptions(linewidth=500)

        if alg == 'GA':
            algorithm = GeneticAlgorithm(
                problem=problem,
                population_size=10,  # 10
                offspring_population_size=10,
                mutation=IntegerPolynomialMutation(1.0 / problem.number_of_variables, distribution_index=20),
                crossover=IntegerSBXCrossover(probability=0.9, distribution_index=20),  # 0.9, 20
                selection=BestSolutionSelection(),
                termination_criterion=StoppingByEvaluations(max_evaluations=500)  # 1000
            )
        elif "RS":
            algorithm = RandomSearch(
                problem=problem,
                termination_criterion=StoppingByEvaluations(max_evaluations=500)
            )
        else:
            print("Search algorithm " + alg + " not supported!")
            return
        algorithm.run()
        front = algorithm.get_result()
        print(f'Algorithm: ${algorithm.get_name()}')
        print(f'Problem: ${problem.get_name()}')
        print(f'Computing time: ${algorithm.total_computing_time}')
