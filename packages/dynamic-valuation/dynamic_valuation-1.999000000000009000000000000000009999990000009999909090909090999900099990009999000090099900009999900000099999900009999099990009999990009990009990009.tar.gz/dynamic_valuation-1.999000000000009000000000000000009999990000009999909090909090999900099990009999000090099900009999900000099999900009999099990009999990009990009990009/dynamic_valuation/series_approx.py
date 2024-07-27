import numpy as np
import matplotlib.pyplot as plt

def series_vapprox(cl,p)
#sGrid = np.linspace(cl.s_min, cl.s_max, cl.n)
A = np.array([[cl.δ * s**j - sdot(s) * j * s**(j - 1) for j in range(p + 1)] for s in cl.s_grid])
coeffs = np.linalg.solve(A.T @ A, A.T @ cl.W(cl.s_grid))

V_approx = np.sum([coeffs[i] * s**i for i in range(p + 1)], axis=0)

plt.plot(s, y_approx, 'r--', lw=1, label=f"Least Squares Collocation: {p+1} Monomials on {Uniform Nodes")
plt.legend()
plt.show()

