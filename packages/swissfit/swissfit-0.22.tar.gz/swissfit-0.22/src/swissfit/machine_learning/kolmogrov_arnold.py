from functools import partial as _partial # Partial evaluation of functions
import numpy as _numpy # General numerical operations
import gvar as _gvar # GVar Gaussian error propagation
from .neuralnetwork import NeuralNetwork as _NeuralNetwork # Parent neural network class
        
class BSpline(object):
    def __init__(self, xknots, degree):
        if self._xknots is not None: self._xknots = [*xknots].sort()
        else: self._xknots = []
        self._degree = degree
        
    def _basis_atom(self, i, k, x): # Recursive construction of b-spline basis function
        match k:
            case 0: return 1. if self._xknots[i] <= x <= self._xknots[i+1] else 0.
            case _:
                c1 = (x - self._xknots[i]) / (self._xknots[i+k] - self._xknots[i])
                c2 = (self._xknots[i+k+1] - x) / (self._xknots[i+k+1] - self._xknots[i+1])
                return c1 * self._basis_atom(i, k-1, x) + c2 * self._basis_atom(i+1, k-1, x)
        
    def basis(self, i, x): return self._basis_atom(i, self._degree, x)

    def _ilist(self): return range(len(self._xknots) - self._degree - 1)
    _ilist = property(_ilist)
    
    def _bases(self, x): return [*map(_partial(self.basis, x = x), self._ilist)]

    def set_xknots(self, xknots):
        self._xknots = [*xknots]
        self._xknots.sort()
    
    def __call__(self, x, p): return _numpy.dot(p, self._bases(x))
        
class _KolmogrovArnoldLayer(object):
    def __init__(self, nl, degree, layer_tag, activation, approximate_activation):
        self._layer_tag = layer_tag
        self._nl = range(nl)
        if hasattr(degree, len): self._spline = [BSpline(None, degree[n]) for n in self._nl]
        else: self._spline = [BSpline(None, degree) for n in self._nl]
        self._act = {
            'linear': self.identity,
            'relu': self.RELU,
            'gelu': {
                True: self.GELU_approximation,
                False: self.GELU
            }[approximate_activation],
            'elu': self.ELU,
            'silu': self.SiLU,
            'tanh': self.tanh,
            'sigmoid': self.sigmoid,
            None: None
        }[activation]
        
    def _spline_weight(self, p, i, j):
        return p[self._layer_tag + '.weight(' + ','.join([*map(str, [i,j])]) + ')']

    def _activation_weight(self, p, i, j):
        return p[self._layer_tag + '.activation(' + ','.join([*map(str, [i,j])]) + ')']

    def _activation(self, x, p):
        return p[0] * self._act(x)
    
    def _node_term(self, x, p, n, m):
        match self._act:
            case None: return self._spline[n](x, self._p(p, n, m)) 
            case _:
                result = self._spline[n](x, self._spline_weight(p, n, m))
                result += self._activation_weight(p, n, m)[0] * self._act(x)
                return result
                
    def _node(self, n, xknots, p):
        self._spline[n].set_xknots(xknots)
        return sum(self._node_term(xknot, p, n, m) for m, xknot in enumerate(xknots))
        
    def __call__(self, xknots, p):
        return [*map(_partial(self._node, xknots = xknots, p = p), self._nl)]
    
class KolmogrovArnoldNetwork(_NeuralNetwork):
    """ Kolmogrov-Arnold Network
    
    Python implementation of the Kolmogrov-Arnold network
    described in arXiv:2404.19756
    
    """
    def __init__(self, topo):
        super().__init__(topo = topo)
        self._construct_network()

    def _construct_network(self):
        self._layers = [
            _KolmogrovArnoldLayer(
                lyr['out'],
                lyr['degree'] if 'degree' in lyr.keys() else 3,
                lyr_tag,
                lyr['activation'] is 'activation' in lyr.keys() else None,
                lyr['approx_activation'] if 'approx_activation' in lyr.keys() else False
            ) for lyr_tag, lyr in self._topo.items()
        ]  

    # Need to write method for initialization
        
    def __call__(self, x, p):
        result = x
        for layer in self._layers: result = layer(result, p)
        return result
