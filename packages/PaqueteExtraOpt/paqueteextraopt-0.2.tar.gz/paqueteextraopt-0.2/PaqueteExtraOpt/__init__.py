from .MetodosMultivariables.randomwalked import caminata_aleatoria
from .MetodosMultivariables.cauchy import cauchy
from .MetodosMultivariables.Reeves import fletcherReeves
from .MetodosMultivariables.HookeJeeves import hooke_jeeves
from .MetodosMultivariables.NelderMead import nelder_mead
from .MetodosMultivariables.newton import newton

from .MetodosUnivariables.Fibonacci import fibonacci_search
from .MetodosUnivariables.biseccion import biseccion
from .MetodosUnivariables.BusquedaDorada import busquedaDorada
from .MetodosUnivariables.IntervalHalving import interval_halving_method
from .MetodosUnivariables.Secante import secante
from .MetodosUnivariables.NewtonRaph import newton_raphson

from .FuncionesPrueba.FuncionesMultivariables import ackley, rastrigin, himmelblau, sphere, shekel, threehumpcamel, styblinskitang, beale, booth, bunkin, crossintray, easom, eggholder, goldstein, holdertable, levi, matyas, mccormick, rosenbrock, schaffer2, schaffer_n4
from .FuncionesPrueba.FuncionesUnivariables import f1, f2, f3, f4