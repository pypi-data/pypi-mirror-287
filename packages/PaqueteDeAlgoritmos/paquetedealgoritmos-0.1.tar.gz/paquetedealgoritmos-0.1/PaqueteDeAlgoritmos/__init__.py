from .FuncionesPrueba.FuncionesMultivariables import ackley, beale, booth, bunkin, crossintray, easom, eggholder, goldstein, himmelblau, holdertable, levi, matyas, mccormick, rastrigin, rosenbrock, schaffer2,schaffer_n4, shekel, sphere, styblinskitang, threehumpcamel
from .FuncionesPrueba.FuncionesUnivariables import f1, f2, f3, f4

from .MetodosMultivariables.caminataAleatoria import caminata_aleatoria
from .MetodosMultivariables.cauchy import cauchy
from .MetodosMultivariables.fletcherReeves import fletcherReeves
from .MetodosMultivariables.hookeJeeves import hooke_jeeves
from .MetodosMultivariables.nelderMeadSimplex import nelder_mead
from .MetodosMultivariables.newton import newton

from .MetodosUnivariables.biseccion import biseccion
from .MetodosUnivariables.busquedaDorada import busquedaDorada
from .MetodosUnivariables.fibonacci import fibonacci_search
from .MetodosUnivariables.intervalHalving import interval_halving_method
from .MetodosUnivariables.newtonRaphson import newton_raphson
from .MetodosUnivariables.secante import secante