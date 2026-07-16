import numpy as np

ventas_rionegro = [2.8, 3.1, 2.5, 3.4, 2.9, 3.6, 2.7, 3.0, 3.3, 2.6,
                   3.8, 2.4, 3.2, 2.9, 3.5, 3.1, 2.8, 3.9, 2.6, 3.0]

q1 = np.percentile(ventas_rionegro, 25)
q2 = np.percentile(ventas_rionegro, 50)
q3 = np.percentile(ventas_rionegro, 75)

print(f'Q1={q1}, Q2={q2}, Q3={q3}')
