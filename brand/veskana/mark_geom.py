"""Merkteken: echte druppel met afgeronde punt, doorgesneden door de filterspleet."""
import math

CX, CY, R = 50.0, 66.0, 26.0     # kamer (onderste vorm)
PHI       = math.radians(61.8)     # waar de zijkant de cirkel raakt
TIP_W, TIP_Y, APEX_Y = 6.0, 16.0, 7.5
T3        = (0.34, -0.94)        # richting waarmee de zijkant bij de punt aankomt
HANDLE    = 0.31
GAP_TOP = 45.0                   # de spleet loopt tot aan het raakpunt van de kamer

TLx, TLy = CX - R*math.sin(PHI), CY - R*math.cos(PHI)
TRx      = CX + R*math.sin(PHI)
P0 = (TLx, TLy)
P3 = (CX - TIP_W, TIP_Y)
_t0 = (math.cos(PHI), -math.sin(PHI))
_len = math.hypot(P3[0]-P0[0], P3[1]-P0[1])
_a = HANDLE*_len
C1 = (P0[0] + _a*_t0[0], P0[1] + _a*_t0[1])
C2 = (P3[0] - _a*T3[0], P3[1] - _a*T3[1])
CURVE = (P0, C1, C2, P3)

def _lerp(a, b, t): return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
def bez(c, t):
    a, b, d = _lerp(c[0],c[1],t), _lerp(c[1],c[2],t), _lerp(c[2],c[3],t)
    e, f = _lerp(a,b,t), _lerp(b,d,t)
    return _lerp(e,f,t)
def split(c, t):
    a, b, d = _lerp(c[0],c[1],t), _lerp(c[1],c[2],t), _lerp(c[2],c[3],t)
    e, f = _lerp(a,b,t), _lerp(b,d,t)
    g = _lerp(e,f,t)
    return (c[0],a,e,g), (g,f,d,c[3])
def t_at_y(c, y):
    lo, hi = 0.0, 1.0
    for _ in range(60):
        m = (lo+hi)/2
        if bez(c, m)[1] > y: lo = m
        else: hi = m
    return (lo+hi)/2

t_top = t_at_y(CURVE, GAP_TOP)
_, TOP_SEG  = split(CURVE, t_top)          # van de spleet naar de punt

def mir(p): return (100.0-p[0], p[1])
def f(p): return f"{p[0]:.2f},{p[1]:.2f}"

# punt: vloeiende kap, hoogte APEX_Y, raaklijn sluit aan op de zijkanten
_m = (TIP_Y-APEX_Y)/(0.75*abs(T3[1]))
K1 = (CX-TIP_W + _m*T3[0], TIP_Y + _m*T3[1])
K2 = mir(K1)
TIPL, TIPR = (CX-TIP_W, TIP_Y), (CX+TIP_W, TIP_Y)

a0,a1,a2,a3 = TOP_SEG
MARK_TRI = (f"M{f(a0)} C{f(a1)} {f(a2)} {f(a3)} "
            f"C{f(K1)} {f(K2)} {f(TIPR)} "
            f"C{f(mir(a2))} {f(mir(a1))} {f(mir(a0))} Z")

MARK_BOWL = f"M{TLx:.2f},{TLy:.2f} A{R:g},{R:g} 0 1 0 {TRx:.2f},{TLy:.2f} Z"

MARK_TOP, MARK_BOT = APEX_Y, CY + R
MARK_L,  MARK_R    = TLx, TRx
if __name__ == "__main__":
    print("punt y=%.1f  spleet %.1f..%.2f (%.1f)  kamer tot y=%.0f" % (APEX_Y, GAP_TOP, TLy, TLy-GAP_TOP, MARK_BOT))
    print("breedte inkt %.2f .. %.2f" % (MARK_L, MARK_R))
