
def central_difference_1(f, x, delta_x):
    return (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

def central_difference_2(f, x, delta_x):
    return (f(x + delta_x) - (2 * f(x)) + f(x - delta_x)) / (delta_x ** 2)

def delta_x_func(x):
    if abs(x) > 0.01:
        x = 0.01 * abs(x) 
    else: 
        return 0.0001
    return x

def bisection_method( a, b, epsilon, delta_x,funcion):
    #step 1
    max_iter=100
    if (central_difference_1(funcion, a, delta_x) < 0) and (central_difference_1(funcion, b, delta_x) > 0):
        x1 = a
        x2 = b
    else:
        print("La función no cumple con la condición")
        return [a,b]
    
    iteraciones = 0

    while abs(x1 - x2) > epsilon and iteraciones < max_iter:
        #step 2
        z = (x1 + x2) / 2
        # print('z: ',z)
        f_z = central_difference_1(funcion, z, delta_x)
        #step 3
        if abs(f_z) <= epsilon:
            return [x1, x2] 
        elif f_z < 0:
            x1 = z
        elif f_z > 0:
            x2 = z
            
        iteraciones += 1

    return [x1, x2]