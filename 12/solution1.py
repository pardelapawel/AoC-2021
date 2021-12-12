#!/bin/python
import sys
import graphviz

def print_graph(g):
    draw_g = graphviz.Graph('G', filename='graph1.gv', engine='circo')
    seen = set()
    for k in g:
        for v in g[k]:
            if k.isupper():
                draw_g.node(k,color='aquamarine3',style='filled')
            if k == 'start':
                draw_g.node(k,color='chartreuse2',style='filled')
            if k == 'end':
                draw_g.node(k,color='cadetblue',style='filled')
            if (k,v) not in seen:
                draw_g.edge(k, v)
                seen.add((k, v))
                seen.add((v, k))
    draw_g.view()



def find_all_paths__(graph, node_from, visited, path):
    if node_from.islower():
        visited.add(node_from)
    path.append(node_from)

    if node_from == 'end':
        #print(path)
        return [path]
    else:
        all_paths = []
        for node in graph[node_from]:
            if node not in visited:
                paths = find_all_paths__(graph, node, visited.copy(), path.copy())
                #print(paths)
                if paths:
                    all_paths.extend(paths)
    return all_paths

def find_all_paths(graph, node_from):
    visited = set()
    path = []
    return find_all_paths__(graph, node_from, visited, path)


#def find_all_paths(graph, start, visited=None, indent=""):
#    def p(string):
#        print(f'{indent.ljust(30)}{string}')
#    p(f"looking for {start}")
#    if start == 'end':
#        return [[start]]
#    if visited is None:
#        my_visited = set()
#    else:
#        my_visited = visited.copy()
#
#    my_visited.add(start)
#    all_paths = []
#    next_nodes = graph[start]
#    for node in next_nodes:
#        p(f"checking for {node}")
#        if node in my_visited and node.islower():
#            p(f"skipping {node} visited={node in my_visited} lower={node.islower()}")
#            continue
#        found_paths = find_all_paths(graph, node, my_visited, f"{indent}{start}>")
#        p(f"extended paths from {start} via {node} = {found_paths}")
#        all_paths.extend(found_paths)
#        my_visited.add(node)
#    res = [[start] + path for path in all_paths]
#    p(res)
#    return res



def main():
    with open(sys.argv[1]) as input_file:
        g = {}
        for line in input_file.readlines():
            left, right = line.strip().split('-')
            g[left] = g.setdefault(left, [])
            g[left].append(right)
            g[right] = g.setdefault(right, [])
            g[right].append(left)
        all_paths = find_all_paths(g, 'start')
        for path in all_paths:
            print(path)
        print(g)
        print(len(all_paths))
        #print_graph(g)




if __name__ == "__main__":
    main()

