from main import *
from rk4_plots import plot_rk


def ode_system(u):
    return np.array(
        [-Decay.dBi209 * u[0], Decay.dBi209 * u[0] - Decay.dBi210 * u[1], Decay.dBi210 * u[1] - Decay.dPo210 * u[2]])


dt = 86400
time = 365


def rk_method(func, u0, dt, time):
    u = np.zeros((time+1, len(u0)))

    u[0] = u0
    for i in range(time):
        k1 = dt*func(u[i])
        k2 = dt*func(u[i]+k1/2)
        k3 = dt * func(u[i] + k2 / 2)
        k4 = dt*func(u[i]+k3)
        u[i+1] = u[i] + (k1+2*k2+2*k3+k4)/6
    return u


u0 = [Init.Bi209_0, Init.Bi210_0, Init.Po210_0]
u = rk_method(ode_system, u0, dt, time)

if __name__ == '__main__':
    Polonium_problem = rk_method(ode_system, u0, dt, time)
    plot_rk(Polonium_problem)