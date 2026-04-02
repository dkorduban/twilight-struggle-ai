Treating this as a **zero-sum matrix game** with payoff = **USSR win rate**, the Nash equilibrium is **mixed**, not pure.

There is **no pure Nash equilibrium** because:

* USSR’s row security values (row minima) are
  `[65.0, 64.9, 63.6, 62.0, 63.5, 61.6]`, so the **maximin** is **65.0** at `ussr=0.5`.
* US’s column security values (column maxima) are
  `[71.8, 69.5, 69.9, 66.8, 67.6, 68.1]`, so the **minimax** is **66.8** at `us=2.0`.

Since `65.0 < 66.8`, there is no saddle point.

## Mixed-strategy Nash equilibrium

### USSR strategy

* `ussr=0.5`: **33.96%**
* `ussr=1.0`: **32.29%**
* `ussr=1.5`: **0%**
* `ussr=2.0`: **0%**
* `ussr=3.0`: **33.74%**
* `ussr=5.0`: **0%**

### US strategy

* `us=0.5`: **0%**
* `us=1.0`: **0%**
* `us=1.5`: **37.75%**
* `us=2.0`: **61.08%**
* `us=3.0`: **1.17%**
* `us=5.0`: **0%**

## Game value

Expected USSR win rate at equilibrium:

**66.0874%**

So the corresponding US value is:

**33.9126%**

In words: USSR should randomize almost evenly between `0.5`, `1.0`, and `3.0`; US should play mostly `2.0`, often `1.5`, and almost never `3.0`.

Code used in essence:

```python
import numpy as np
from scipy.optimize import linprog

A = np.array([
    [70.5,68.3,67.8,65.0,67.6,65.9],
    [71.8,66.9,64.9,66.8,67.2,68.0],
    [71.2,67.7,69.9,63.6,65.7,67.1],
    [69.3,69.5,67.2,64.3,62.0,68.1],
    [68.1,67.9,65.5,66.5,63.5,65.5],
    [64.9,64.3,63.2,62.1,61.6,64.4],
])

m, n = A.shape

# USSR LP: maximize v s.t. p>=0, sum p=1, A^T p >= v
c = [0]*m + [-1]
A_ub = [list(-A[:,j]) + [1] for j in range(n)]
b_ub = [0]*n
A_eq = [[1]*m + [0]]
b_eq = [1]
bounds = [(0,None)]*m + [(None,None)]

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
print(res.x[:m], res.x[-1])
```

Because your entries are empirical win rates, small probability masses like the US `3.0` weight may not be very stable if the underlying estimates are noisy.
