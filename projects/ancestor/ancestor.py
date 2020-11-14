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
    for i in ancestors:
        if i in graph:
            graph[i[0]].append(i[1])
        else:
            graph[i[0]] = [i[1]]

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
            for i in graph[currVert]:
                newPath = list(currPath)
                newPath.append(i)
                stack.append(newPath)
                if len(newPath) > len(answer):
                    answer = newPath
    return answer[-1]