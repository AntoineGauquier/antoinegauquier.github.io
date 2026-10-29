import sys
import math
import heapq

class SommetAStar:
    def __init__(self, id, h):
        self.id = id
        self.parent = None
        self.g = math.inf
        self.h = h

    def __lt__(self, other):
        return (self.g + self.h, self.id) < (other.g + other.h, other.id)



n, e, s, g = [int(i) for i in input().split()]

graphe = []
adjacences = [[] for _ in range(n)]

iter = 0
for i in input().split():
    node = int(i)
    graphe.append(SommetAStar(iter, node))
    iter += 1

for i in range(e):
    x, y, c = [int(j) for j in input().split()]
    adjacences[x].append((y, c))
    adjacences[y].append((x, c))


file_p = []
closed = set()
open_set = set()

start_node = graphe[s]
start_node.g = 0
heapq.heappush(file_p, (start_node.g + start_node.h, start_node))
open_set.add(start_node.id)

while file_p:
    f_u, _, u = heapq.heappop(file_p)

    if u.id in closed:
        continue

    closed.add(u.id)

    print(u.id, u.g + u.h)

    if u.id == g:
        break

    for v in adjacences[u.id]:
        v_dest, v_poids = v
        neighbor = graphe[v_dest]
        curr_node_cost = u.g + v_poids
        if v_dest in closed:
            continue

        if curr_node_cost < neighbor.g:
            neighbor.g = curr_node_cost
            neighbor.parent = u.id
            heapq.heappush(file_p, (neighbor.g + neighbor.h, neighbor))
            open_set.add(neighbor.id)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)