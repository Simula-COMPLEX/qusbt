# QuSBT: Search-based Testing of Quantum Programs

This repository contains the code to reproduce the results of the paper "Generating Failing Test Suites for Quantum Programs with Search", published in 13th Symposium on Search-Based Software Engineering (SSBSE 2021).

It also contains the original results reported in the paper.

## Structure of the repository

* Folder *benchmarkPrograms* contains the visualizations of the circuits of the 6 original programs and their 30 faulty versions (see Table 1 in the paper).
* Folder *code* contains the code of QuSBT
    * subfolder *code/programs* contains the Python code of the 6 original programs and their 30 faulty versions
* Folder *experimentalResults* reports the data of all the experiments conducted for the paper

## Installation of QuSBT
QuSBT uses [Qiskit](https://qiskit.org/) as quantum framework, [jMetalPy](https://github.com/jMetal/jMetalPy) as search framework, and [R](https://www.r-project.org/) as framework for doing statistical tests.

The following steps should guarantee to have a working installation of QuSBT:
* Install Anaconda. You can download Anaconda for your OS from [https://www.anaconda.com/](https://www.anaconda.com/)
    * e.g.
        * wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
        * bash Anaconda3-2020.11-Linux-x86_64.sh
* Create an environment (e.g., with name "myenv")
    * conda create -n myenv python=3.7 scipy numpy rpy2
* Activate the environment, and install qiskit and jmetalpy
    * conda activate myenv
    * pip install qiskit
    * pip install jmetalpy
* In your Anaconda installation, change file the file envs/myenv/lib/python3.7/site-packages/jmetal/operator/__init__.py
    * "DifferentialEvolutionCrossover" must be changed in "DifferentialEvolutionCrossover, IntegerSBXCrossover"

## Running QuSBT

QuSBT can be run as follows.

First, you need to activate the conda environment:

```
conda activate myenv
```

Then, you can start the program (from the repository root) as follows:

```
python code/QuSBT.py num_qubits benchmark_name specification_name search_algorithm
```

where:
* *num_qubits* is the number of input qubits of the program specification: see Table 1 in the paper (column |I|)
* *benchmark_name* is the name of the benchmark program: concatenate the name of the *Program* and the index (1, ..., 5) of the *Faulty version* in Table 1 in the paper (e.g., *AS_1*)
* *specification_name* is the name of the original program acting as program specification: see column *Program* in Table 1 in the paper (e.g., *AS*)
* *search_algorithm* identifies whether the genetic algorithm (GA), or Random Search (RS) must be used (use *GA* or *RS*)

Results of the search will be saved in folder *results*

## Paper
X. Wang, P. Arcaini, T. Yue, S. Ali. Generating Failing Test Suites for Quantum Programs with Search. In 13th Symposium on Search-Based Software Engineering (SSBSE 2021) [[doi](https://doi.org/10.1007/978-3-030-88106-1_2)]
