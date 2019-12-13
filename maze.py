import random

SEED = None
SIZE = (10, 10)
FOG = 2
N, S, E, W = range(4)


def flip(d):
    if d == N:
        return S
    if d == S:
        return N
    if d == E:
        return W
    if d == W:
        return E


def complement(w):
    d, (x, y) = w

    if d == N:
        return (S, (x, y - 1))
    if d == S:
        return (N, (x, y + 1))
    if d == E:
        return (W, (x + 1, y))
    if d == W:
        return (E, (x - 1, y))


class Maze:
    def __init__(self, walls=None, size=SIZE, seed=SEED):
        self.size = size
        self.position = (0, 0)
        self.start = (N, self.position)
        self.finish = (S, (size[0] - 1, size[1] - 1))
        self.path, self.direction = [self.start[1]], flip(self.start[0])

        # If no walls provided, generate some random ones
        if not walls:
            walls = self.generate(seed)

        self.walls = set([(d, cell) for d, cell in walls])

        self.walls.remove(self.start)
        self.walls.remove(self.finish)

    def move(self, d):
        x, y = self.position

        if (d, (x, y)) in self.walls:
            raise Exception("There is a wall!")
        if (d, (x, y)) == self.start:
            raise Exception("You cannot go back this way!")
        if (d, (x, y)) == self.finish:
            raise Exception("You made your way out!")

        if d == N:
            self.position = (x, y - 1)
        if d == S:
            self.position = (x, y + 1)
        if d == E:
            self.position = (x + 1, y)
        if d == W:
            self.position = (x - 1, y)

        self.direction = d
        self.path.append(self.position)

    def generate(self, seed):
        # Implementation of https://en.wikipedia.org/wiki/
        # Maze_generation_algorithm#Randomized_Prim's_algorithm

        def divides(w):
            if w[0] == N:
                return [w[1], (w[1][0], w[1][1] - 1)]
            if w[0] == S:
                return [w[1], (w[1][0], w[1][1] + 1)]
            if w[0] == E:
                return [w[1], (w[1][0] + 1, w[1][1])]
            if w[0] == W:
                return [w[1], (w[1][0] - 1, w[1][1])]

        def outbound(cell):
            if cell[0] < 0 or cell[0] >= self.size[0]:
                return True
            if cell[1] < 0 or cell[1] >= self.size[1]:
                return True
            return False

        if seed is not None:
            random.seed(seed)

        start = (random.choice(range(self.size[0])),
                 random.choice(range(self.size[1])))
        visited = set([start])
        waiting = [(d, start) for d in [N, S, E, W]]
        walls = set((d, (x, y)) for d in [N, S, E, W]
                    for x in range(self.size[0])
                    for y in range(self.size[1]))

        while waiting:
            w = random.choice(waiting)
            c0, c1 = divides(w)

            if c0 in visited and c1 not in visited:
                cell = c1
            elif c1 in visited and c0 not in visited:
                cell = c0
            else:
                cell = None

            if cell is not None and not outbound(cell):
                visited.add(cell)
                walls.remove(w)
                walls.remove(complement(w))

                for v in [(d, cell) for d in [N, S, E, W]]:
                    if v in walls:
                        waiting.append(v)

            waiting.remove(w)

        return walls

    def __str__(self, fog=FOG):
        def angle(x, y):
            intersection = [w for w in [(N, (x, y)), (S, (x - 1, y - 1)),
                                        (E, (x - 1, y - 1)), (W, (x, y))]
                            if w in self.walls or complement(w) in self.walls]
            if len(intersection) == 2:
                if [d for (d, _) in intersection] == [N, S]:
                    return "-"
                elif [d for (d, _) in intersection] == [E, W]:
                    return "|"
            return "+"

        if fog is None:
            x0, x1 = 0, self.size[0]
            y0, y1 = 0, self.size[1]

        else:
            x0 = max(0, self.position[0] - fog + 1)
            x1 = min(self.size[0], self.position[0] + fog)
            y0 = max(0, self.position[1] - fog + 1)
            y1 = min(self.size[1], self.position[1] + fog)

        s = ""

        # Print the first line of walls to the North
        for i in range(x0, x1 + 1):
            s += angle(i, y0)

            if i == x1:
                s += "\n"
            elif (N, (i, y0)) in self.walls:
                s += "---"
            else:
                s += "   "

        for j in range(y0, y1):
            # Print vertical walls and path traces
            for i in range(x0, x1):
                s += "| " if (W, (i, j)) in self.walls else "  "

                if (i, j) == self.path[-1]:
                    if self.direction == N:
                        s += "^"
                    if self.direction == S:
                        s += "v"
                    if self.direction == E:
                        s += ">"
                    if self.direction == W:
                        s += "<"
                elif (i, j) in self.path:
                    s += "x"
                else:
                    s += " "

                s += " "

            if (E, (x1 - 1, j)) in self.walls:
                s += "|\n"
            else:
                s += " \n"

            # Print horizontal walls with '+' when walls intersect
            for i in range(x0, x1 + 1):
                s += angle(i, j + 1)

                if i == x1:
                    s += "\n"
                elif (S, (i, j)) in self.walls:
                    s += "---"
                else:
                    s += "   "

        return s

    def print_all(self):
        print(self.__str__(fog=None))


if __name__ == "__main__":
    Maze().print_all()
