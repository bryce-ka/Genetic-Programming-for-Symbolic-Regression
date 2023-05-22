class Node:
    def __init__(self, data):
        self.parent = None
        self.data = str(data)
        self.left = None
        self.right = None
    
    # def __str__(self, level=0):
    #     ret = "\t"*level+repr(self.data)+"\n"
    #     for child in range(1):
    #         if child == 0:
    #             ret += self.left.__str__(level+1)
    #         if child == 1:
    #             ret += self.right.__str__(level+1)
                
    #     return ret
    

    # def __repr__(self):
    #     return '<tree node representation>'
        
    #needs information about the parent, child left and child right, value which could be a string and cast it
# not much needs to happen in this class

