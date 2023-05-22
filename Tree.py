import pandas as pd
from sklearn.metrics import mean_squared_error as mse 
import random
from Node import Node
import sklearn
# from geneticProgram import printInorder

class Tree:
    # needs evaluate function that gives a number when its done
    # a collection of linked node objects
    # this is going to be the main work horse with at least a mutate and cross over method
    # trees should start pretty small because they can grow but you can have some variety
    # generate random invidiual
    # usually only stashes the root nod
    def __init__(self, depth, root, amount_x):
        operators = ['+', '-', '*','/']# 'log']
        # constants = ['-5', '-4', '-3', '-2', '-1', '1', '2', '3', '4', '5', 'x']
        # const_index = len(constants) - 1
        ops_index = len(operators) - 1
        specificOperator = operators[random.randint(0,ops_index)]
        self.depth = depth
        # self.root = self.make_tree(depth, None, 0, None)
        if (not isinstance(root, Node)):
            self.root = self.make_tree(depth, None, 0, None)
            if (amount_x == 3):
                val1 = self.insert_x('x1')
                while (val1 == 0): #insert necessary x variables. making sure that x variables aren't replacing each other
                    val1 = self.insert_x('x1')
                val2 = self.insert_x('x2')
                while (val2 == 0):
                    val2 = self.insert_x('x2')
                val3 = self.insert_x('x3')
                while (val3 == 0):
                    val3 = self.insert_x('x3')
            else:
                self.insert_x('x')

        else:
            self.root = root
        # print(specificOperator)
        
    def make_tree(self, depth, currNode, level, root):
        operators = ['+', '-', '*','/']
        constants = ['-5','-4', '-2.3','-3', '-2', '-1', '1','1.4' '2', '3', '3.7', '4', '5'] 
        const_index = len(constants) - 1
        ops_index = len(operators) - 1
        if level == depth:
            # currNode = Node(constants[random.randint(0,19)])
            # print(currNode.data)
            currNode.left = None
            currNode.right = None
            return root
        else:
            if level == 0:
                root = Node(operators[random.randint(0,ops_index)])
                root.left = Node(operators[random.randint(0,ops_index)])
                root.left.parent = root
                root.right = Node(operators[random.randint(0,ops_index)])
                root.right.parent = root 
                self.make_tree(depth,root.left, level + 1, root), self.make_tree(depth, root.right, level + 1, root)
            elif level == depth -1:
                currNode.left = Node(constants[random.randint(0,const_index)])
                currNode.left.parent = currNode
                currNode.right = Node(constants[random.randint(0,const_index)])
                currNode.right.parent = currNode
                self.make_tree(depth, currNode.left, level + 1, root),self.make_tree(depth, currNode.right, level + 1, root)

            else:
                currNode.left = Node(operators[random.randint(0,ops_index)])
                currNode.left.parent = currNode
                currNode.right = Node(operators[random.randint(0,ops_index)])
                currNode.right.parent = currNode
                self.make_tree(depth, currNode.left, level + 1, root), self.make_tree(depth, currNode.right, level + 1, root)

        return root
    def insert_x(self, x_var): #randomly places x at the latest level in every new tree
        cur_node=self.root
        for i in range(self.depth):
            lor = random.randint(0,1)
            if lor == 0:
                if cur_node.left != None:
                    cur_node =cur_node.left
                else:
                    break
            elif lor ==1:
                if cur_node.right != None:
                    cur_node =cur_node.right
                else:
                    break
        if (cur_node.data == 'x1' or cur_node.data == 'x2' or cur_node.data == 'x3'):
            return 0
        else:
            cur_node.data = x_var
            return 1

    
    def printInorder(self, root, indent):
        if root:
            indent+=1
    
            # First recur on left child
            self.printInorder(root.left, indent)
    
            # then print the data of node
            print("\t"*indent, root.data)
    
            # now recur on right child
            self.printInorder(root.right, indent)

    def multi_evaluate(self, currNode, x1_val, x2_val, x3_val):
        operators = ['+', '-', '*','/']
        # self.printInorder(currNode, -1)
        # print()
        if ((currNode.left and currNode.right) == None):
            if currNode.data == "x1":
                return x1_val
            elif currNode.data == "x2":
                return x2_val
            elif currNode.data == "x3":
                return x3_val
            return float(currNode.data)
        else:
            if (currNode.data == '-'):
                return self.multi_evaluate(currNode.left, x1_val, x2_val, x3_val) - self.multi_evaluate(currNode.right, x1_val, x2_val, x3_val)
            if (currNode.data == '+'):
                return self.multi_evaluate(currNode.left, x1_val, x2_val, x3_val) + self.multi_evaluate(currNode.right, x1_val, x2_val, x3_val)
            if (currNode.data == '*'):
                return self.multi_evaluate(currNode.left, x1_val, x2_val, x3_val) * self.multi_evaluate(currNode.right, x1_val, x2_val, x3_val)
            if (currNode.data == '/'):
                denominator = self.multi_evaluate(currNode.right, x1_val, x2_val, x3_val)
                if(denominator != 0 ):
                    return self.multi_evaluate(currNode.left, x1_val, x2_val, x3_val) / denominator
                else:
                    return 1
    
    
    def evaluate(self, currNode, x_val):
        operators = ['+', '-', '*','/']
        # self.printInorder(currNode, -1)
        # print()
        if ((currNode.left and currNode.right) == None):
            if currNode.data == "x":
                return x_val
            return float(currNode.data)
        else:
            if (currNode.data == '-'):
                return self.evaluate(currNode.left, x_val) - self.evaluate(currNode.right, x_val)
            if (currNode.data == '+'):
                return self.evaluate(currNode.left, x_val) + self.evaluate(currNode.right, x_val)
            if (currNode.data == '*'):
                return self.evaluate(currNode.left, x_val) * self.evaluate(currNode.right, x_val)
            if (currNode.data == '/'):
                denominator = self.evaluate(currNode.right, x_val)
                if(denominator != 0 ):
                    return self.evaluate(currNode.left, x_val) / denominator
                else:
                    return 1

    def fitness(self, df):
        guess = []
        for index, row in df.iterrows():
            guess.append(self.evaluate(self.root, row["x"]))
        preds = pd.DataFrame(guess)
        fit_val = sklearn.metrics.mean_squared_error(df['f(x)'], preds)
        # fit_val = sklearn.metrics.mean_squared_error(df['f(x)'], guess)
        return fit_val
    
    def multi_fitness(self, df):
        guess = []
        for index, row in df.iterrows():
            guess.append(self.multi_evaluate(self.root, row["x1"], row["x2"], row["x3"]))
        preds = pd.DataFrame(guess)
        fit_val = sklearn.metrics.mean_squared_error(df['f(x)'], preds)
        # fit_val = sklearn.metrics.mean_squared_error(df['f(x)'], guess)
        return fit_val
    def get_copy(self):
        new_root = Node(self.root.data)
        new_tree = Tree(self.depth, new_root, 3)
        self.copy(self.root, new_tree.root)
        return new_tree



    def copy(self, og_node, new_node):
        if og_node is not None:
            # new_node.data = og_node.data
            if (og_node.right is not None): 
                new_node.right = Node(og_node.right.data)
                new_node.right.parent = new_node
                self.copy(og_node.right, new_node.right)
            else:
                new_node.right = None
            if (og_node.left is not None):
                new_node.left = Node(og_node.left.data)
                new_node.left.parent = new_node
                self.copy(og_node.left, new_node.left)
            else:
                new_node.left = None
            return new_node.data
        
    def mutation(self): #need to select for mutation based on fitness 
    #This asexual mutation operation is typically performed sparingly (with a low probability of, say, 1% during each generation of the run)
        new_tree = self.get_copy()
        
        path = random.randint(1, new_tree.depth - 1)
        cur_node=new_tree.root
        
        
        for i in range(path):
            lor = random.randint(0,1)
            if lor == 0:
                if cur_node.left != None:
                    cur_node =cur_node.left
                else:
                    break
            elif lor ==1:
                if cur_node.right != None:
                    cur_node =cur_node.right
                else:
                    break
        # build a new tree starting with current node 
        depth =2
        attachment = Tree(depth, None, 1)
        new_tree.depth+=depth
        attachment.root.parent = cur_node.parent
        cur_node.data = attachment.root.data
        cur_node.left = attachment.root.left 
        cur_node.right = attachment.root.right
        return new_tree
    
    def crossover(self, tree2): #apply to 85/90% of population 
        #randomly choose a node from self
        #randomly choose a node from tree2 
        #substitute tree2 node with self node
        tree1 = self.get_copy()
        tree2 = tree2.get_copy()
        t1 = random.randint(1, self.depth)
        t2 = random.randint(0, tree2.depth-1)

        cur_node=tree1.root 
        depth1 = tree1.depth
        for i in range(t1): #randomly choose a node from self 
            lor = random.randint(0,1)
            if lor ==0: #randomly going down left or right side
                if cur_node.left != None:
                    depth1-=1
                    cur_node =cur_node.left
                else:
                    break
            elif lor ==1:
                if cur_node.right != None:
                    depth1-=1
                    cur_node =cur_node.right
                else:
                    break

        tree1_node = cur_node 

        cur_node=tree2.root 
        depth2 = tree2.depth # depth of sub tree from node 
        for i in range(t2): #randomly choose a node from self 
            lor = random.randint(0,1)
            if lor ==0:
                if cur_node.left != None:
                    depth2-=1
                    cur_node =cur_node.left
                else:
                    break
            elif lor ==1:
                if cur_node.right != None:
                    depth2-=1
                    cur_node =cur_node.right
                else: 
                    break

        tree2_node = cur_node
        operators = ['+', '-', '*','/']
        val = tree2_node.data
        if operators.count(val) == 0:
            tree2_node = tree2_node.parent
        if depth2>depth1:   
            tree1.depth += depth2
        tree1_node.data = tree2_node.data
        tree1_node.left = tree2_node.left
        tree1_node.right = tree2_node.right 

        return tree1
    def reproduction(self):
        return self.get_copy()
