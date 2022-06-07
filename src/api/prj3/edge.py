class Edge:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def nodes_vector(self, whole):
        vector = [0 for _ in range(whole)]
        vector[self.begin], vector[self.end] = 1, 1
        print(vector)
