from regpy.operators.volterra import Volterra
from regpy.hilbert import L2
from regpy.discrs import UniformGrid
from regpy.solvers import HilbertSpaceSetting
from regpy.solvers.irgnm_semismooth import IRGNMSemiSmooth
import regpy.stoprules as rules

import numpy as np
import logging
import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)-20s :: %(message)s'
)

grid = UniformGrid(np.linspace(0, 2*np.pi, 200))
op = Volterra(grid, exponent=1)

exact_solution = np.sin(grid.coords[0])
exact_data = op(exact_solution)
noise = 0.1 * op.domain.randn()
data = exact_data + noise
init = op.domain.zeros()

setting = HilbertSpaceSetting(op=op, Hdomain=L2, Hcodomain=L2)

solver = IRGNMSemiSmooth(setting, data, psi_minus=-1, psi_plus=1, regpar=1, regpar_step=0.9, init=init)
stoprule = (
    rules.CountIterations(100) +
    rules.Discrepancy(
        setting.Hcodomain.norm, data,
        noiselevel=setting.Hcodomain.norm(noise),
        tau=1.1
    )
)

reco, reco_data = solver.run(stoprule)

plt.plot(grid.coords[0], exact_solution.T, label='exact solution')
plt.plot(grid.coords[0], reco, label='reco')
plt.plot(grid.coords[0], exact_data, label='exact data')
plt.plot(grid.coords[0], data, label='data')
plt.plot(grid.coords[0], reco_data, label='reco data')
plt.legend()
plt.show()
