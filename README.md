# Método de Euler en Python

Este proyecto resuelve una ecuación diferencial separable de forma analítica y
compara su solución exacta con el método de Euler en **t ∈ [0, 1]**, con
paso **h = 0.2**.

## Problema y solución analítica

Seleccionamos el problema de valor inicial:

$$\frac{dy}{dt}=y,\qquad y(0)=1.$$

Separamos las variables, para y ≠ 0:

$$\frac{dy}{y}=dt.$$

Integramos ambos lados:

$$\ln|y|=t+C.$$

Al despejar obtenemos y(t) = A eᵗ. La condición inicial y(0) = 1 implica A = 1.
Por tanto, la solución exacta es:

$$\boxed{y(t)=e^t}.$$

La ecuación también admite y = 0, excluida al dividir entre y; esta solución
no satisface la condición inicial del problema.

## Aproximación con Euler

Euler explícito utiliza la pendiente en el punto actual:

$$t_n=nh,\qquad y_{n+1}=y_n+h f(t_n,y_n).$$

Aquí f(t, y) = y, h = 0.2 y y₀ = 1. Así:

$$y_{n+1}=1.2y_n,\qquad y_n=(1.2)^n.$$

Se requieren cinco pasos para llegar a t = 1; se muestran seis puntos contando
el inicial. El primer paso es y₁ = 1 + 0.2(1) = 1.2.

| t | Euler | Solución exacta eᵗ | Error absoluto |
|---:|---:|---:|---:|
| 0.0 | 1.000000 | 1.000000 | 0.000000 |
| 0.2 | 1.200000 | 1.221403 | 0.021403 |
| 0.4 | 1.440000 | 1.491825 | 0.051825 |
| 0.6 | 1.728000 | 1.822119 | 0.094119 |
| 0.8 | 2.073600 | 2.225541 | 0.151941 |
| 1.0 | 2.488320 | 2.718282 | 0.229962 |

El error absoluto es |eᵗ − yₙ|. En t = 1, Euler aproxima y(1) por 2.488320,
con un error absoluto de aproximadamente 0.229962. En este caso Euler
subestima la solución, que es creciente y convexa. La tabla redondea a seis
decimales; el programa conserva la precisión de punto flotante durante el cálculo.

## Ejecución

Se necesita Python 3. No se requieren paquetes externos: `math` forma parte
de la biblioteca estándar.

```bash
python3 euler.py
```

El programa imprime la ecuación, la solución exacta y la tabla comparativa.
La función `aproximar_euler()` devuelve los datos para usarlos desde otro programa.
