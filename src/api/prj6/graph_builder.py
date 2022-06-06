import random

from src.api.prj6.directed_graph import SimpleGraph


class GraphBuilder:
    """Tworzy różne rodzaje grafów"""

  

   
    @staticmethod
    def get_random_2D_graph(
        size=20, x_min=-50, x_max=50, y_min=-50, y_max=50
    ) -> SimpleGraph:
        filename = f"{size}_coordinates.tmp"
        with open(filename, "w") as f:
            for _ in range(size):
                x = random.randint(x_min, x_max)
                y = random.randint(y_min, y_max)
                f.write(f"{x} {y}\n")
        g = SimpleGraph().from_coordinates(filename)
        return g