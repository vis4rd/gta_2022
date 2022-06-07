class Node:
    @staticmethod
    def create_copy(node):
        copy = Node(node.number)
        copy.neighbours = [n for n in node.neighbours]
        return copy

    def __init__(self, number):
        self.number = number
        self.neighbours = []

    def neighbours_list(self):
        print("{}: {}".format(self.number + 1, [n + 1 for n in self.neighbours]))

    def neighbours_vector(self, whole):
        vector = [0 for _ in range(whole)]

        for i in range(len(self.neighbours)):
            vector[self.neighbours[i]] = 1

        print(vector)

    def neighbour_delete(self, index):
        for i, n in enumerate(self.neigbours):
            if n == index:
                del self.neighbours[i]
                break
