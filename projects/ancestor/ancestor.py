from collections import deque
"""
Understand
With a graph of ancestors to find oldest one by getting the one with the longest path to a end.

Plan
Place data into a graph
create a algarthem to do a bft and return the ancestor from the largest path.
if there is no ansestors return -1

Excute

Review
"""




def earliest_ancestor(ancestors, starting_node):
    graph = dict()
    answer = []
    for i in range(len(ancestors)):
        parent, child = ancestors[i][0], ancestors[i][1]
        if child in graph:
            graph[child].append(parent)
        else:
            graph[child] = [parent]

    stack = deque()
    found = set()
    if starting_node not in graph:
        return -1
    stack.append([starting_node])
    while stack:
        currPath = stack.popleft()
        currVert = currPath[-1]
        if currVert not in found:
            found.add(currVert)
            if currVert not in graph:
                continue
            for i in graph[currVert]:
                newPath = list(currPath)
                newPath.append(i)
                stack.append(newPath)
                if len(newPath) > len(answer):
                    answer = newPath
    return answer[-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
if __name__ == '__main__':
    print(earliest_ancestor(test_ancestors, 6))