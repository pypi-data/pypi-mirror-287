
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

def newton_raphson_method(funcion, i_guess, delta_fun, epsilon):
    x = i_guess
    k = 1
    max_iter=100
    while k < max_iter:
        #step1
        delta_x = delta_fun(x)
        f_derivada1 = central_difference_1(funcion, x, delta_x)
        #step2
        f_derivada2= central_difference_2(funcion, x, delta_x)
        # print("fderivada1",f_derivada1)
        # print("fderivada2",f_derivada2)
        #step 3
        x_k1 = x - f_derivada1 / f_derivada2
        # print("x2",x_k1)
        f_x_k1 = central_difference_1(funcion,x_k1,delta_x)
        # print("fxk1",f_x_k1)
        if abs(f_x_k1) < epsilon:
            return x_k1
        x = x_k1
        k += 1
    
    return x
