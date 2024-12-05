# =====================================================
#
# File Name: solve.py
# Date of Creation: Sat 15 May 2021 20:05:05
# Author: user Tan
# Description: This python script is used to solve systems of linear equations
# https://stackoverflow.com/questions/58878594/solving-simultaneous-equations-with-python
# =====================================================
# =====================================================


from sympy import Eq, solve, pi, integrate, symbols, simplify, inverse_laplace_transform, laplace_transform, diff, Symbol
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import numpy as np

def nsv(f, x, x_0, uncertainty = 10e-10):
    # f = sympy function in terms of x
    # x = sympy variable
    # x_0 = number

    f_ = diff(f, x)
    x_diff = 1 / uncertainty
    x_n = x_0
    newton = f / f_
    while abs(x_diff) > uncertainty:
        x_diff = newton.subs(x, x_n)
        x_n -= x_diff
    return x_n

def sv(eqs, exact = False):
    # if the eqs passed in is comma separated then split into list by the commas
    if type(eqs) == str:
        eqs =  eqs.split(",");

    # adding an =0, in case we forget to put it in
    eqs = [eq if ("=" in eq) else eq + '= 0' for eq in eqs];


    # fancy math stuff from stack overflow
    transformations=(standard_transformations + (implicit_multiplication_application,))
    eqs_sympy = [Eq(parse_expr(e.split('=')[0], transformations=transformations),
                    parse_expr(e.split('=')[1], transformations=transformations))
                 for e in eqs]
    sol = solve(eqs_sympy)

    # figuring out what to do with whether we want the exact value or the estimated value
    if not exact:
        if type(sol) == dict:
            sol = [sol];
        sol = [[{s:ss[s].evalf()} for s in ss] for ss in sol];

    return sol;

def P2R(radii, angles, deg = False):
    #polar to rectangular coordinates
    return radii * np.exp(1j*angles * (1 + deg * (np.pi / 180 - 1)))

def R2P(x, deg = False):
    #rectangular to polar coordinates
    return abs(x), np.angle(x, deg)

def L(f):
    # laplace transform of a function (t)
    t, s = symbols("t s")
    return laplace_transform(f, t, s, noconds=True)

def invL(F):
    # inverse laplace transform of a function (s)
    t, s = symbols("t s")
    return inverse_laplace_transform(F, s, t)

def ll(*args):
    return 1/sum(1/i for i in args);

class Materials:
    """
    NA is the avogrados number (atoms / mol)
    """
    NA = 6.023 * 10**23

class Crystal:
    R = symbols("R")
    a = None
    n = None
    R = None

class FCC(Crystal):
    R = symbols("R")
    a = 2 * np.sqrt(2) * R
    n = 4
    V = a ** 3

class BCC(Crystal):
    R = symbols("R")
    a = 4 / np.sqrt(3) * R
    n = 2
    V = a ** 3
    # V = 12.31 * R ** 3 # note that this is exactly correct as well

class HCP(Crystal):
    R = symbols("R")
    a = 2 * R
    c = 1.623 * a # note that this constant is fixed
    n = 6
    V = 3 * np.sqrt(3) / 2 * a ** 2 * c



class Si:
    """
    k = boltzmann constant (8.62 * 10 ** -5 eV / K)
    E_g = semiconductor bandgap energy (eV)
    T = absolute room temperature (K)
    B = Si, material-dependent parameter, 1.08 * 10 ** 31 K ** -3 * cm ** -6
    q = charge of electron 1.60217662 * 10**-19
    V_t = einstein's diffusion / mobility constant =  26e-3, room temperature # kt_q = k * T / q, note that this is in electron volts!!
    epsilon_s = dielectric constant of Si
    """
    B = 1.08 * 10 ** 31
    E_g = 1.12
    T = 300
    k = 8.62 * 10 ** -5
    q = 1.60217662 * 10**-19
    V_t = 26e-3
    epsilon_s = 11.7 * 8.85 * 10 ** -14



if __name__ == '__main__':
    #eqs = 'x + y = 4, x + 2y = 5'
    #eqs1 = ['2w + x + 4y + 3z = 5x + 5y', 'w - 2x + 3z = 3x + 5y + 5x**2/5', '3w + 2x - y + z = -1', '4x - 5z = -3']
    #eqs2 = '2w + x + 4y + 3z = 5x + 5y, w - 2x + 3z = 3x + 5y + 5x**2/5, 3w + 2x - y + z = -1, 4x - 5z = -3'
    #eqs3 = "y ** 2 = x, y**2 - x**2 = -12"
    #eqs4 = "a_b + c_d = 2, c_d * 2 + a_b = 5"
    #eqs5 = "-3.4386 = 1.1462v_g1 + 0.1338x, -4.5846 = 1.5282v_g1 + 0.0764y, v_g1 = 0.15x + 0.2y"

    #print(f"sv(eqs) = {sv(eqs)}");
    #print(f"sv(eqs1, False) = {sv(eqs1, False)}");
    #print(f"sv(eqs2, True) = {sv(eqs2, True)}");
    #print(f"sv(eqs3, True) = {sv(eqs3, True)}");
    #print(f"sv(eqs3, False) = {sv(eqs3, False)}");
    #print(f"sv(eqs4) = {sv(eqs4)}");
    
    R1, R2, L, C = 1, 4, 1/2, 1/8;
    v_cp = 20 * R2/(R1 + R2);
    print(f"v_cp = {v_cp}");

    v = f'v ** 2 + {1/(R2 * C) + R1 /L} * v + {(R1 + R2)/(L * C * R2)}'
    print(f"v = {v}");
    print(f"sv(v) = {sv(v)}");

    print(f"sv('cos(x) = 5') = {sv('cos(x) = 1')}");
    print(f"sv('theta ** 2 + theta  = 4') = {sv('theta ** 2 + theta  = 4')}");
    print(f"sv('x = conjugate(1+4j)') = {sv('x = conjugate(1+4j)')}");
    print(f"sv('x = re(1 + 5j) + im(1+ 5j)') = {sv('x = re(1 + 5j) + im(1+ 5j)')}");
    
    print(f"sv('conjugate(x) + 1 + 2j') = {sv('conjugate(x) + 1 + 2j')}");
    # print(f"sv('x = sin(x)') = {sv('x = sin(x)')}");
    
    print(f"Si.B = {Si.B}")



    # for making matplotlib work in darkmode
    plt.tick_params(axis='x', colors='red')
    plt.tick_params(axis='y', colors='red')
