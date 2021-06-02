# -*- coding: utf-8 -*-

__all__ = ['k_shortest_paths']


import networkx as nx

def k_shortest_paths(G, source, target, K=1, weight='weight', all_kshortest = False):
    
    if source == target:
        return (0, [source]) 
    
    A = []
    all_length = []
    
    B_length, B = nx.single_source_dijkstra(G, source, target, weight=weight)
    
    if K ==1:
        return B_length, B
    A.append(B)
    all_length.append(B_length)
    
    if target not in A[0]:
        raise nx.NetworkXNoPath("node %s not reachable from %s" % (source, target))
        
    for k in range(1, K):

        for i in range(len(A[-1]) - 1):
            spur_node = A[-1][i]
            root_path = A[-1][:i + 1]
            
            if weight:
                root_path_length = get_path_length(G, root_path, weight)
            
            edges_removed = []
            if  weight:
                edge_attr = []
            for path in A:
                if root_path == path[:i + 1]:
                    u = path[i]
                    v = path[i + 1]
                    if (u,v) not in edges_removed:
                        if  weight:
                            edge_attr.append(G[u][v][weight])
                        G.remove_edge(u, v)
                        edges_removed.append((u, v))
            
            for node in root_path[:-1]:
                for u, v, attr in list(G.edges(node, data=True)):
                    if  weight:
                        edge_attr.append(attr[weight])
                    G.remove_edge(u,v)
                    edges_removed.append((u,v))
            
            try:
                spur_path_length, spur_path = nx.single_source_dijkstra(G, spur_node, target, weight=weight)  
            except:
                spur_path_length = 0
                spur_path = []
                
            total_path = root_path[:-1] + spur_path
            if weight:
                total_path_length = root_path_length + spur_path_length         
            else:
                total_path_length = i + spur_path_length
            if total_path_length > all_length[-1]:
                if B:
                    if total_path_length < B_length:
                        B = total_path
                        B_length = total_path_length
                    else:
                        B = total_path
                        B_length = total_path_length
                    
            for w in range(len(edges_removed)):
                u = edges_removed[w][0]
                v = edges_removed[w][1]
                G.add_edge(u,v)
                if  weight:
                    G.edges[u,v][weight]=edge_attr[w]
        
        if B:
            A.append(B)
            all_length.append(B_length)
        else:
            break
    if all_kshortest:
        return (all_length, A)
    
    return (all_length[-1], A[-1])

def get_path_length(G, path, weight='weight'):
    length = 0

    if len(path) > 1:
        for i in range(len(path)-1):
            u = path[i]
            v = path[i + 1]
            
            length += G.edges[u,v][weight]
    
    return length    
    
G = nx.DiGraph()
G.add_edge('C', 'D',length = 3)
G.add_edge('C', 'E',length = 2)
G.add_edge('D', 'F',length = 4)
G.add_edge('E', 'D',length = 1)
G.add_edge('E', 'F',length = 2)
G.add_edge('E', 'G',length = 3)
G.add_edge('F', 'G',length = 2)
G.add_edge('F', 'H',length = 1)
G.add_edge('G', 'H',length = 2)

print(k_shortest_paths(G, 'C', 'H', 3, "length",False)) 
