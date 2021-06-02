Calcula o caminho mais curto K para uma determinada problema, utilizando o algoritmo de Yen.

 
 Este script usa a biblioteca networkx do python3 para a estrutura de dados do grafo.


    Parâmetros:
   
    G: NetworkX Graph ou DiGraph
    
    source: node
       node inicial
    target: node
       node final
       
    K: inteiro, opcional (padrão = 1)
       
    
    peso: string, opcional (padrão = 'peso')
       Chave de dados da aresta correspondente ao peso da aresta
       Para grafo sem peso, passe ''.
    
    all_kshortest: booleano, opcional (padrão = False)
       Se verdadeiro, retorna todos os caminhos mais curtos anteriores
    
   Saida: comprimentos, 
   
      
    Exemplos: 
    
    >>> G = nx.complete_graph (5)
    >>> imprimir (k_shortest_paths (G, 0, 4, 4))
    ([1, 2, 2, 2], [[0, 4], [0, 1, 4], [0, 2, 4], [0, 3, 4]])
    
    OBS:
    Os atributos de peso da aresta devem ser numéricos e não negativos.
    As distâncias são calculadas como somas de arestas ponderadas percorridas.


