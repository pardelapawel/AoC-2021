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

def is_small(cave):
    if cave in 'start end'.split():
        return False
    return cave.islower()

def is_big(cave):
    return cave.isupper()

def find_all_paths__(graph, node_from, visited, path, double_allowed=True, indent=""):
    def p(*strings):
        print(f'{indent}',*strings)

    if node_from.islower():
        visited[node_from] -= 1
    path.append(node_from)

    if node_from == 'end':
        #print(f'{indent}            {",".join(path)}')
        print('-'*len(indent) + '-'.join(path), f'next: {",".join([f"{n}({visited[n]})" for n in graph[node_from]])}')
        return [path]
    else:
        p('-'.join(path), f'next: {",".join([f"{n}({visited[n]})" for n in graph[node_from]])}')
        all_paths = []
        #print(f'{indent}for node in {graph[node_from]}')
        for node in sorted(graph[node_from]):
            #print(f'{indent}{node} = {visited[node]}')
            if visited[node] > 0:
                if double_allowed and is_small(node):
                    paths = []
                    paths += find_all_paths__(graph, node, visited.copy(), path.copy(), double_allowed, indent + "  ")
                    visited[node] += 1
                    p(f'double is {node}')
                    #print(f'Increased {node} to {visited[node]}')
                    double_allowed = False
                    paths += find_all_paths__(graph, node, visited.copy(), path.copy(), double_allowed, indent + " |")
                    if paths:
                        all_paths.extend(paths.copy())
                else:
                    paths = find_all_paths__(graph, node, visited.copy(), path.copy(), double_allowed, indent + "  ")
                    all_paths.extend(paths.copy())
            #else:
                #print(f'Skipping {node_from} -> {node} with {visited[node]}')
        return all_paths

def find_all_paths(graph, node_from):
    visited_limits = dict.fromkeys(graph.keys(), 0)
    for k in visited_limits.keys():
        visited_limits[k] = 1
        if is_big(k):
            visited_limits[k] = 2
    #visited['start'] = 1
    #visited['end'] = 1
    path = []
    return find_all_paths__(graph, node_from, visited_limits, path)



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
        #for no, path in enumerate(sorted(list(set([','.join(x) for x in all_paths])))):
        #    print(no, path)
        print(g)
        print(len(all_paths))
        #print_graph(g)




if __name__ == "__main__":
    main()

