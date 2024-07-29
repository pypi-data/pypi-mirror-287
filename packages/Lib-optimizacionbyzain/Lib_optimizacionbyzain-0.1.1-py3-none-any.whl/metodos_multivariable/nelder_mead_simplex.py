import numpy as np

def simplex_search_meth(xstart,func):
    N = len(xstart)
    alfa = 1.0
    gamma = 2.0
    beta = 0.5
    tolerancia = 1e-5
    iter_max = 1000
    
    delta1 = (np.sqrt(N + 1) + N - 1) / (N * np.sqrt(2)) * alfa
    delta2 = (np.sqrt(N + 1) - 1) / (N * np.sqrt(2)) * alfa
    
    simplex = np.zeros((N + 1, N))
    simplex[0] = xstart
    
    for i in range(1, N + 1):
        punto = xstart.copy()
        punto[i - 1] += delta1
        for j in range(N):
            if j != i - 1:
                punto[j] += delta2
        simplex[i] = punto

    for iteracion in range(iter_max):
        simplex = sorted(simplex, key=func)
        simplex = np.array(simplex)
        
        centroide = np.mean(simplex[:-1], axis=0)
        reflexion = 2 * centroide - simplex[-1]
        
        if func(reflexion) < func(simplex[0]):
            expansion = centroide + gamma * (centroide - simplex[-1])
            nuevo_punto = expansion if func(expansion) < func(reflexion) else reflexion
        elif func(reflexion) >= func(simplex[-2]):
            if func(reflexion) < func(simplex[-1]):
                contraccion_fuera = centroide + beta * (reflexion - centroide)
                nuevo_punto = contraccion_fuera
            else:
                contraccion_dentro = centroide - beta * (centroide - simplex[-1])
                nuevo_punto = contraccion_dentro
        else:
            nuevo_punto = reflexion
        
        simplex[-1] = nuevo_punto
        
        if np.sqrt(np.mean([(func(x) - func(centroide))**2 for x in simplex])) <= tolerancia:
            break

    simplex = sorted(simplex, key=func)
    simplex = np.array(simplex)
    
    return simplex[0]