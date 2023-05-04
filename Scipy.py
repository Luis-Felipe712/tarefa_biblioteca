# Importa a biblioteca SciPy e a função integrate
from scipy import integrate

# Define a função que deseja integrar
def f(x):
    return x**2

# Calcula a integral da função f no intervalo [0,1] utilizando a função quad da biblioteca integrate
result, error = integrate.quad(f, 0, 1)

# Imprime o valor da integral da função f no intervalo [0,1]
print("Valor da integral: ", result)
