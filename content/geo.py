"""Map projection shared by build.py (church dots, lines, labels) and tools/make_map.py (states, coastline).

Albers equal-area conic, the projection used for most U.S. maps, fitted to a 620 x 560 box that
covers Texas to New England and down to the Florida Keys. Change VIEW or the region, then run
python3 tools/make_map.py so the outlines and the dots stay aligned.
"""
import math

VIEW = (620, 560)
_LON0, _LAT0, _P1, _P2 = -84.0, 32.0, 24.0, 44.0
# region shown: (west, south, east, north) in degrees, plus a margin in pixels
REGION = (-100.5, 23.8, -66.8, 47.2)
PAD = 14

_n = (math.sin(math.radians(_P1)) + math.sin(math.radians(_P2))) / 2
_c = math.cos(math.radians(_P1)) ** 2 + 2 * _n * math.sin(math.radians(_P1))
_rho0 = math.sqrt(_c - 2 * _n * math.sin(math.radians(_LAT0))) / _n


def _albers(lon, lat):
    theta = _n * math.radians(lon - _LON0)
    rho = math.sqrt(max(_c - 2 * _n * math.sin(math.radians(lat)), 0)) / _n
    return rho * math.sin(theta), _rho0 - rho * math.cos(theta)


def _fit():
    w, s, e, n = REGION
    pts = [_albers(lon, lat) for lon in [w + (e - w) * i / 40 for i in range(41)] for lat in (s, n)]
    pts += [_albers(lon, lat) for lat in [s + (n - s) * i / 40 for i in range(41)] for lon in (w, e)]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    k = min((VIEW[0] - 2 * PAD) / (max(xs) - min(xs)), (VIEW[1] - 2 * PAD) / (max(ys) - min(ys)))
    ox = (VIEW[0] - k * (max(xs) - min(xs))) / 2 - k * min(xs)
    oy = (VIEW[1] - k * (max(ys) - min(ys))) / 2 + k * max(ys)
    return k, ox, oy


_K, _OX, _OY = _fit()


def project(lon, lat):
    """(lon, lat) in degrees -> (x, y) in the map's SVG coordinates."""
    x, y = _albers(lon, lat)
    return round(_OX + _K * x, 1), round(_OY - _K * y, 1)
