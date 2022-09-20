from main import *
from rk4_plots import plot_rk


def ode_system(u):
    """
    Function that represents the system of differential equations.
    For this problem, the system has three equations.

    Args:
        u : array representing the equations.

    Returns:
        np.array(
        [-Decay.dBi209 * u[0], Decay.dBi209 * u[0] - Decay.dBi210 * u[1], Decay.dBi210 * u[1] - Decay.dPo210 * u[2]]
        )

        Array that represents the right-hand-side of each differential equation

    """
    return np.array(
        [-Decay.dBi209 * u[0], Decay.dBi209 * u[0] - Decay.dBi210 * u[1], Decay.dBi210 * u[1] - Decay.dPo210 * u[2]]
    )


# Setting parameters
dt = Par.time_step
time = Par.total_time


def rk_method(func, u0, dt, time):
    """
    Function who implements Runge-Kutta method to 4th order.

    Args:
        func : right-hand-side of the ode;

        u0 : vector of the initial nuclide concentrations (it's a 1 row, 3 columns vector like);

        dt(int) : time increment;

        time(int) : duration;

    Returns:
        u : updated by Runge-Kutta method array.

    """

    # Initialize the vector
    u = np.zeros((time+1, len(u0)))

    # Collect inside the first row the value of u0 who takes the three initial conditions
    u[0] = u0

    # Loop
    for i in range(time):
        k1 = dt*func(u[i])
        k2 = dt*func(u[i]+k1/2)
        k3 = dt * func(u[i] + k2 / 2)
        k4 = dt*func(u[i]+k3)
        u[i+1] = u[i] + (k1+2*k2+2*k3+k4)/6

    return u


# Initialize u0 with initial conditions
u0 = [Init.Bi209_0, Init.Bi210_0, Init.Po210_0]

# Calling the function and collect the results into u array
u = rk_method(ode_system, u0, dt, time)

if __name__ == '__main__':
    Polonium_problem = rk_method(ode_system, u0, dt, time)
    plot_rk(Polonium_problem)