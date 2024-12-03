def plot_geometry(*p_A):
    """
    Función que grafica una figura dado una 
    cantidad de puntos distintos
    """
    import matplotlib.pyplot as plt
    X = []
    Y = []
    for a in range(len(p_A)):
        X.append(p_A[a].x)
        Y.append(p_A[a].y)
    
    X.append(p_A[0].x)  # Hay que repetir de nuevo el primero.
    Y.append(p_A[0].y)  # Para que pueda cerrarse la curva.

       # Rellenar el interior de la figura (mejor que usar fill.between)
    plt.fill(X, Y, color='pink', alpha=0.7)  # alpha ajusta la opacidad 
    
    
    plt.plot(X, Y, color='pink')
