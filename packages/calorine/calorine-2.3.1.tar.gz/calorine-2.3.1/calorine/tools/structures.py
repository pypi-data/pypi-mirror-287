from ase import Atoms
from ase.constraints import ExpCellFilter
from ase.optimize import BFGS, LBFGS, FIRE, GPMin
from ase.optimize.sciopt import SciPyFminBFGS


def relax_structure(structure: Atoms,
                    fmax: float = 0.001,
                    steps: int = 500,
                    minimizer: str = 'bfgs',
                    constant_cell: bool = False,
                    constant_volume: bool = False,
                    **kwargs) -> None:
    """Relaxes the given structure.

    Parameters
    ----------
    structure
        atomic configuration to relax
    fmax
        if the absolute force for all atoms falls below this value the relaxation is stopped
    steps
        maximum number of relaxation steps the minimizer is allowed to take
    minimizer
        minimizer to use; possible values: 'bfgs', 'lbfgs', 'fire', 'gpmin', 'bfgs-scipy'
    constant_cell
        if True do not relax the cell or the volume
    constant_volume
        if True relax the cell shape but keep the volume constant
    kwargs
        keyword arguments to be handed over to the minimizer; possible arguments can be found
        in the `ASE documentation <https://wiki.fysik.dtu.dk/ase/ase/optimize.html>`_
    """
    if structure.calc is None:
        raise ValueError('Structure has no attached calculator object')
    if constant_cell:
        ucf = structure
    else:
        ucf = ExpCellFilter(structure, constant_volume=constant_volume)
    kwargs['logfile'] = kwargs.get('logfile', None)
    if minimizer == 'bfgs':
        dyn = BFGS(ucf, **kwargs)
        dyn.run(fmax=fmax, steps=steps)
    elif minimizer == 'lbfgs':
        dyn = LBFGS(ucf, **kwargs)
        dyn.run(fmax=fmax, steps=steps)
    elif minimizer == 'bfgs-scipy':
        dyn = SciPyFminBFGS(ucf, **kwargs)
        dyn.run(fmax=fmax, steps=steps)
    elif minimizer == 'fire':
        dyn = FIRE(ucf, **kwargs)
        dyn.run(fmax=fmax, steps=steps)
    elif minimizer == 'gpmin':
        dyn = GPMin(ucf, **kwargs)
        dyn.run(fmax=fmax, steps=steps)
    else:
        raise ValueError(f'Unknown minimizer: {minimizer}')
