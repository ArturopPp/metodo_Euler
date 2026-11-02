"""Resuelve y' = y, y(0) = 1 mediante Euler en [0, 1], con h = 0.2."""

from math import exp


def aproximar_euler():
    """Devuelve filas (t, aproximación, solución exacta, error absoluto)."""
    h = 0.2
    y = 1.0
    filas = []
    for n in range(6):
        t = n * h
        exacta = exp(t)
        filas.append((t, y, exacta, abs(exacta - y)))
        if n < 5:
            y = y + h * y
    return filas


def main():
    print("Ecuación: y' = y; condición inicial: y(0) = 1")
    print("Solución exacta: y(t) = exp(t)")
    print("Método de Euler: intervalo [0, 1], h = 0.2\n")
    print(f"{'t':>5} {'Euler':>12} {'Exacta':>12} {'Error absoluto':>16}")
    for t, y, exacta, error in aproximar_euler():
        print(f"{t:5.1f} {y:12.6f} {exacta:12.6f} {error:16.6f}")


if __name__ == "__main__":
    main()
