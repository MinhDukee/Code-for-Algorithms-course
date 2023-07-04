dataset = open("huffmann.txt", "rt")
dataset = dataset.readlines()
graph = []
for i in dataset:
    graph.append([int(str(i.split('\n')[0]))])
    
graph.pop(0)
dictionary = {i[0] : 0  for i in graph}
def merge(graphe, val1, val2):
    graphe.pop(graphe.index(val1))
    dictionaryadd(val1)
    graphe.pop(graphe.index(val2))
    dictionaryadd(val2)
    graphe.append([val2,val1])

def dictionaryadd(val):
    if len(val) == 1:
        dictionary[val[0]] += 1
    else:
        dictionaryadd(val[0])
        dictionaryadd(val[1])


def sorting(e):
    if len(e) == 1:
        return e[0]
    else:
        return sorting(e[0]) + sorting(e[1])
        
while len(graph) > 1:
    graph.sort(key=sorting)
    merge(graph,graph[0],graph[1])

dictionary = dict(sorted(dictionary.items()))
print("Min: " + str(dictionary[list(dictionary)[-1]]))
print("Max: " + str(dictionary[list(dictionary)[0]]))