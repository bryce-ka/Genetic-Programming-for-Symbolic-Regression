import pandas as pd
from Node import Node
from Tree import Tree
# !pip install scikit-learn
import random
import sklearn
import time 
import math

# ds1 = pd.read_csv("dataset1.csv")
# ds1
    

def get_equation(root):
    if(not root):
        return 
    
    if(not root.left and not root.right):
        print(root.data, end = " ")
        return 
    
    if root.left:
        print('('+get_equation(root.left))

    if root.right:
        print(get_equation(root.left))
    

def runTournament(fitness_all, tournament, treeDict, flag): #Tournament Selection Implementation
    count = 0
    while (count != 4): #tournament size is 4
        indexFound = random.randint(0, len(fitness_all) -1)
        tournament.append(fitness_all[indexFound]) #you could go back and make sure nothing is chosen twice
        count+=1
    tournament.sort() #order the results of the tournament to find the winner
    winner = treeDict[tournament[0]]
    runnerUp = treeDict[tournament[1]]
    if (flag == 1):
        return winner.crossover(runnerUp)
        #crossover
    elif (flag == 0):
        return winner.reproduction()
    elif (flag == -1):
        return winner.mutation()
        #mutation
    return 0



def setUpTreeGen(treeList, df): #sets up variables for each new generation
    treeDict = {}
    fitness_all = []
    for i in range(len(treeList)): #seed population
        # treeFitness = treeList[i].fitness(df) #calculate fitness of new tree
        treeFitness = treeList[i].fitness(df) #calculate fitness of new tree
        fitness_all.append(treeFitness) #adds fitness to list of fitnesses
        treeDict[treeFitness] = treeList[i]  #pairs tree fitness with the tree
    return treeDict, fitness_all 
            
def evolution(df):
    count = 0 
    best = 10000
    populationSize = 30 
    crossOverPortion = (math.trunc(populationSize *.9))
    reproductionPortion = (math.trunc(populationSize *.08))
    mutationPortion = (math.trunc(populationSize *.02))
    treeList =[]
    best_tree = 0
    for i in range(populationSize): #seed population
        treeList.append(Tree(2, None, 1))
    treeDict, fitness_all = setUpTreeGen(treeList, df)

    # written_equation = ""
    while best > 6 and count <= 30: #keep making new generations until there have been 50 or the mean squared error is less than 6
        # print("generation: ", count)
        next_gen = []
        switchMethod = 1
        while (len(next_gen) < len(treeList)): #keep running tournaments until next_gen is filled out
            tournament = [] #tournament selection
            if (switchMethod >= crossOverPortion): #handles method for evolution divied as according to article
                next_gen.append(runTournament(fitness_all, tournament, treeDict, 1))
            elif (switchMethod >= reproductionPortion):
                next_gen.append(runTournament(fitness_all, tournament, treeDict, 0))
            elif (switchMethod >= mutationPortion):
                next_gen.append(runTournament(fitness_all, tournament, treeDict, -1))
            switchMethod += 1

        # written_equation = ""
        treeList = next_gen
        treeDict, fitness_all = setUpTreeGen(treeList, df) #refreshes variables for newGeneration

        best = min(fitness_all) #checks to see if the best has been reached
        best_tree_index = fitness_all.index(best)
        best_tree = treeList[best_tree_index]
        # print(fitness_all)
        # get_equation(best_tree.root, written_equation, "c")
        count+=1

    # print("made it through the weeds")
    # print(len(treeList))
    # print(best)
    # print(best_tree)
    return best_tree, best 

def bloatControl():
    df = pd.read_csv("dataset3.csv") #do the reading outside and pass in the dataframe
    divide = math.trunc((1/3)*len(df.index)) #find which value would represent the top 1/3rd
    bestOptions = {}
    treeList = []
    fitnessList = []
    trainingSet = df.iloc[divide:] #make the training set the latter 2/3rds of the data set
    testSet = df.iloc[:divide] #the test set the first 1/3rd of the data set
    fit_all = []
    count = 1
    for i in range(10): #run the evolution 10 different times to get ten different models
        tree, fitness = evolution(trainingSet)
        # bestOptions[fitness] = tree
        treeList.append(tree)
        fitnessList.append(fitness)
        print("times rans: ")
        print(count)
        count+=1

    for i in range(len(treeList)):
        potential = treeList[i].fitness(testSet)
        print("option")
        print(i)
        treeList[i].printInorder(treeList[i].root, -1)
        print("fitness")
        print(potential)
        bestOptions[potential] = treeList[i]
        fit_all.append(potential)
    best_fit = min(fit_all)
    print(best_fit)
    # get_equation(bestOptions[best_fit].root)
    return bestOptions[best_fit], best_fit
 
    
    
if __name__ == "__main__":
    tree, fitness = bloatControl()
    print("____________the end_____________")
    tree.printInorder(tree.root, -1)
    print(fitness)