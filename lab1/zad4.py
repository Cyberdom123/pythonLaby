class Tree:
    def __init__(self, value) -> None:
        self.nodeVal = value
        self.nodes = []
        self.id = 0

    def AddNode(self, value):
        tree = Tree(value)
        tree.id = self.id + 1
        self.nodes.append(tree)
    
    def GoThrough(self):
        print(self)
        for node in self.nodes:
            if len(node.nodes) != 0:
                node.GoThrough()
            else:
                print(f"{node}")

    def __str__(self):
        string = ""
        for i in range(self.id):
            string = string + " ";
        string = string + "┗➔"
        return f"{string} Node value: {self.nodeVal}"

tree = Tree(0)
tree.AddNode(3.14)
tree.nodes[0].AddNode(1)
tree.nodes[0].AddNode(3)
tree.nodes[0].nodes[0].AddNode(33)
tree.nodes[0].nodes[0].AddNode(23)
tree.nodes[0].nodes[1].AddNode(11)


tree.GoThrough()