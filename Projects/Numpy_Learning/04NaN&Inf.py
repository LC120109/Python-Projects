import numpy as np

#NaN = not a number ; Inf = infinity

print(np.nan)
print(np.inf)

print(np.isnan(np.nan))
print(np.isinf(np.inf))

print(np.isnan(np.sqrt(-1))) #bc complex numbers = nan
print(np.isinf(np.array([10]) / 0)) #impossibility

