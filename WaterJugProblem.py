import collections
from collections import deque


def BFS(a, b, target):
    m = {}
    isSolveable = False
    path = []
    q = deque()
    q.append((0, 0))
    while len(q) > 0:
        u = q.popleft()
        if (u[0], u[1]) in m:
            continue

        if (u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0):
            continue

        m[(u[0], u[1])] = 1
        path.append([u[0], u[1]])

        if u[0] == target or u[1] == target:
            isSolveable = True
            if u[0] == target:
                path.append((u[0], 0))
            else:
                path.append((0, u[1]))
            for tp in path:
                print('(', tp[0], ',', tp[1], ')')
            break

        q.append([u[0], 0])
        q.append([0, u[1]])
        q.append([u[0],b])
        q.append([a,u[1]])
        for ap in range(max(a,b)+1):
            c = u[0] + ap
            d = u[1] - ap
            if c == a or d == 0:
                q.append([c, d])

            c = u[0] - ap
            d = u[1] + ap
            if c == 0 or d == b:
                q.append([c, d])
    if not isSolveable:
        print('No Solution')


# Driver code
if __name__ == '__main__':
    Jug1, Jug2, target = 10, 7, 2
    print("Path from initial state "
          "to solution state ::")

    BFS(Jug1, Jug2, target)
