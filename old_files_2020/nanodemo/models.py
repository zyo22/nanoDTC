from lmfit import Model, Parameters, Parameter
from nanodemo.functions import *


def hertz_model(data_obj, opt_kwargs={}):
    d, f, t = data_obj.dft

    _hertz = Model(hertz)

    params = Parameters()
    params['a1'] = Parameter(name='a1', value=np.median(f))
    params['b1'] = Parameter(name='b1', value=0, min=-10 * np.median(f))
    params['cp'] = Parameter(name='cp', value=d.max() * 0.7)
    params['k'] = Parameter(name='k', value=20)
    params['bead_radius'] = Parameter(name='bead_radius', value=data_obj.bead_radius, vary=False)

    fitted = _hertz.fit(f, params, x=d)

    return fitted, (d, f, fitted.best_fit)


def hertz_model2(data_obj, opt_kwargs={}):
    d, f, t = data_obj.dft

    _hertz = Model(hertz)

    params = Parameters()
    params['a1'] = Parameter(name='a1', value=np.median(f))
    params['b1'] = Parameter(name='b1', value=0, min=-10 * np.median(f))
    params['cp'] = Parameter(name='cp', value=d.max() * 0.7)
    params['k'] = Parameter(name='k', value=20)
    params['bead_radius'] = Parameter(name='bead_radius', value=data_obj.bead_radius, vary=False)

    fitted = _hertz.fit(f, params, x=d)

    return fitted, (d, f, fitted.best_fit)


def line(data_obj, opt_kwargs={}):
    d, f, t = data_obj.dft

    _line = Model(linear)

    params = Parameters()
    params['m'] = Parameter(name='m', value=np.median(f))
    params['c'] = Parameter(name='c', value=0, min=-10 * np.median(f))

    fitted = _line.fit(f, params, x=d)

    return fitted, (d, f, fitted.best_fit)
