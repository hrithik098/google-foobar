import heapq
from collections import defaultdict


min_steps = 8
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

class Node:
    def __init__(self, x, y, path=0):
        self.x = x
        self.y = y
        self.path = path

    def __hash__(self):
        return hash(tuple(self))

    def __iter__(self):
        for i in [self.x, self.y]:
            yield i

    def __eq__(self, node):
        return self.x == node.x and self.y == node.y


class Find:
    def __init__(self, step, movements):
        self.step = step
        self.movements = movements

    def node(self, position):
        return Node(int(position % self.step) + 1, int(position / self.step) + 1)

    def valid(self, x, y):
        return True if x >= 0 < self.step and y >= 0 < self.step else False

    def path(self, start, end):
        shortest_path = []
        shortest_path.append(start)
        visited = {}
        while shortest_path:
            node = shortest_path.pop(0)
            if node == end:
                return node.path
            if node not in visited:
                visited[node] = True
                for offset in self.movements:
                    x, y = list(tuple(x + y for x, y in zip(tuple(node), offset)))
                    if self.valid(x, y):
                        shortest_path.append(Node(x, y, node.path + 1))

        return float('inf')


def solution(src, dest):
    #Your code here
    matrix = Find(step = min_steps, movements = moves)
    start = matrix.node(src)
    end = matrix.node(dest)
    step = matrix.path(start, end)
    return step

# x= int(input())
# y= int(input())
# print(solution(x,y))