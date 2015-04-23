import math

def f(_wsp, _x):
	_wyn = 0
	for _i in range(0, len(_wsp)):
		_wyn += _wsp[_i] * math.pow(_x, _i)
	return _wyn

def siecz(w, x0, x1):
	g = x1 * f(w, x0) - x0 * f(w, x1)
	d = f(w, x0) - f(w, x1)
	return x1, g / d

def falsi(w, x, a):
	u = (a * f(w, x) - x * f(w, a)) / (f(w, x) - f(w, a))
	print u
	if f(w, u) * f(w, a) > 0:
		return u, a
	else:
		return x, u

def dx(_wsp):
	_nwsp = []
	for _i in range(1, len(_wsp)):
		_nwsp.append(_wsp[_i] * _i)
	return _nwsp

def it(_wsp, _x, _n=10):
	w = _wsp
	dw = dx(w)
	x = _x
	for _i in range(0, _n):
		x -= f(w, x) / f(dw, x)
		print x

def muller(w, x):
	fx = f(w, x)
	dw = dx(w)
	ddw = dx(dw)
	dfx = f(dw, x)
	ddfx = f(ddw, x)
	
	pier = math.sqrt(dfx * dfx - 2 * fx * ddfx)
	x1 = x - (fx - pier) / ddfx
	x2 = x - (fx + pier) / ddfx
	if abs(f(w, x1)) < abs(f(w, x2)):
		return x1
	else:
	 	return x2

def itm(w, x, n=10):
	for i in range(0, n):
		x = muller(w, x)
		print x

def hor(_wsp, _x):
	_nwsp = []
	_tmp = 0
	for _i in range(len(_wsp) - 1, 0, -1):
		_nwsp.append(_wsp[_i] - _tmp)
		_tmp = _x * _nwsp[-1]
	return _nwsp[::-1]	
