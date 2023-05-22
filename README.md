# Genetic-Programming-for-Symbolic-Regression


This repository contains code for implementing genetic programming for symbolic regression. The code uses a genetic algorithm to evolve a population of trees to find the best regression for a given dataset. Our research paper [Using Genetic Programming (GP) to Implement Symbolic Regression.pdf](https://github.com/bryce-ka/Genetic-Programming-for-Symbolic-Regression/blob/main/Using%20Genetic%20Programming%20(GP)%20to%20Implement%20Symbolic%20Regression.pdf) explains our implementation of genetic programming along with our results. 

## Overview

The genetic programming process involves the following steps:

1. Initializing the population: The code seeds the initial population of trees.
2. Fitness evaluation: The fitness of each tree in the population is calculated using a fitness function.
3. Tournament selection: A tournament selection process is used to select trees to create the next generation based on their fitness values.
4. Reproduction, crossover, and mutation: The selected trees undergo reproduction, crossover, or mutation operations to create the next generation of trees.
5. New generation evaluation: The fitness of the new generation of trees is evaluated.
6. Iteration: Steps 3 to 5 are repeated until a termination condition is met (e.g., a maximum number of generations or a fitness threshold).

## Dependencies

The code requires the following dependencies:

- `pandas`: A library for data manipulation and analysis.

You can install the required dependencies using the following command:

```bash
pip install pandas
```

## Usage

To use the code, follow these steps:

1. Prepare your dataset: The code assumes that the dataset is in CSV format. You need to provide the path to your dataset in the `bloatControl` function.

2. Define the fitness function: You need to define a fitness function specific to your problem. The fitness function evaluates the performance of a tree model on the dataset.

3. Run the evolutionary tree modeling process: Call the `bloatControl` function to start the evolution process. This function runs the evolution multiple times and selects the best tree model based on fitness.

4. Interpret the results: The best tree model and its fitness value will be printed at the end of the execution.
