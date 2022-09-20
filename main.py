import numpy as np
from scipy.linalg import expm
from Config import *
from matrix_exp_plots import plot


# Creating coefficient's matrix
A_matrix = np.array([[-Decay.dBi209, 0, 0],
                     [Decay.dBi209, -Decay.dBi210, 0],
                     [0, Decay.dBi210, -Decay.dPo210]])


def matrix_exp(Bi209_t, Bi210_t, Po210_t):

    """
    Function which implements matrix exponential method.

    Args:
        Bi209_t(float) (Bismuth209) : Bismuth209 concentration at time t;
        Bi210_t(float) (Bismuth210) : Bismuth210 concentration at time t;
        Po210_t(float) (Polonium210) : Polonium210 concentration at time t;

    Returns:
        exp_matrix_prod(float) : product between the exponential matrix and the array
                                containing the three concentrations

    Example:
        make an array of [3 = #rows, 1 = #columns] then pass the matrix and the array to np.matmul:
            v = np.array([x, y, z])
            A = np.array([[a, b, c], [d, e, f], [g, h, i]] and take the expm(t * A) to call
            exponentiation method, then use np.matmul(expm(t * A), v).

    """

    exp_matrix_prod = np.matmul(expm(Par.time_step * A_matrix), np.array(([Bi209_t, Bi210_t, Po210_t])))
    return exp_matrix_prod


def main(time, dt):
    """
    Function of the main problem.

    Args:
        time(float) : total duration of the experiment.
        dt(float) : increment.

    Returns:
        sol_updated(float) : 3 columns vector that collects the updated solutions.

    """

    sol_in = [[Init.Bi209_0, Init.Bi210_0, Init.Po210_0]]  # List of the initial nuclide's concentrations

    for i in range(Par.total_time):
        sol_in.append(matrix_exp(sol_in[i][0], sol_in[i][1], sol_in[i][2]))  # Calling the method and iterate

    sol_updated = np.array(sol_in)  # Updating the vector solution

    return sol_updated


if __name__ == '__main__':
    Polonium_problem = main(time=Par.total_time, dt=Par.time_step)  # Calling the method
    plot(Polonium_problem)
