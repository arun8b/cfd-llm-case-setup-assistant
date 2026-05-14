# Sample Session

## User

For a 2D external airfoil RANS case, what boundary conditions and convergence checks should I use?

## Assistant

For an external airfoil case, use a freestream or velocity inlet condition upstream, pressure outlet or farfield downstream, no-slip wall on the airfoil, and empty or symmetry boundaries for a 2D case. The farfield should be sufficiently far from the airfoil to reduce blockage and artificial pressure effects.

Do not rely only on residual convergence. Monitor lift, drag and moment coefficients, because integrated force quantities can still drift even when residuals reduce.

Recommended checks:

- residual histories
- CL/CD/CM convergence histories
- y+ distribution
- mesh quality and wake refinement
- coarse/medium/fine mesh sensitivity
- comparison against reference trends or benchmark data
