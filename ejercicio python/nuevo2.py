import random

def calcular_pi(num_puntos):
    puntos_dentro_circulo = 0

    for _ in range(num_puntos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Calcular la distancia al origen
        if x**2 + y**2 <= 1:
            puntos_dentro_circulo += 1

    # El área del cuadrado es 4 y el área del círculo es π
    pi_estimate = 4 * puntos_dentro_circulo / num_puntos
    return pi_estimate

# Número de puntos a utilizar
num_puntos = 1000000
pi_estimado = calcular_pi(num_puntos)
print(f"Estimación de PI con {num_puntos} puntos: {pi_estimado}")
