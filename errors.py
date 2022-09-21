from runge import u
from main import main
from Config import Par
import matplotlib.pyplot as plt


def difference_in_methods(u):
    """
    Function that computes the difference between matrix exponentiation and Runge-Kutta 4th order.

    It calls methods from main function and runge function and simply collects them into arrays.
    Then, it computes an arithmetic difference between the vector containing matrix exponential method and
    the other with Runge-Kutta.
    The difference is the "distance" between the two.

    Args:
        u (array) : array calculated with Runge-Kutta.

    Returns:
        It returns a list of the difference between the methods.
        list : [err0, err1, err2]

    """
    # Initialize Runge Kutta vectors
    u0 = u[:, 0]
    u1 = u[:, 1]
    u2 = u[:, 2]

    # Computing matrix exponential vectors
    mtx_expm0 = main(Par.total_time, Par.time_step)[:, 0]
    mtx_expm1 = main(Par.total_time, Par.time_step)[:, 1]
    mtx_expm2 = main(Par.total_time, Par.time_step)[:, 2]

    # Computing errors function
    err0 = mtx_expm0 - u0
    err1 = mtx_expm1 - u1
    err2 = mtx_expm2 - u2

    return [err0, err1, err2]


# Calling the method implemented above
err_list = difference_in_methods(u)


def plot_error_functions(err_list):
    """
        Function that plots the difference between matrix exponentiation and Runge-Kutta 4th order.

        Args:
            err_list (list) : list collecting the errors calculated by the function "difference_in_methods".

        Returns:
            list : [fig0, fig1, fig2]

    """
    fig0 = plt.figure()
    plt.plot(err_list[0], 'k', label='Difference between matrix and Runge-Kutta method for Bi-209')
    plt.xlabel('Time [days]')
    plt.ylabel('Error function Bi-209')
    plt.legend(loc=0)
    plt.grid(True)
    plt.show()

    fig1 = plt.figure()
    plt.plot(err_list[1], 'k', label='Difference between matrix and Runge-Kutta method for Bi-210')
    plt.xlabel('Time [days]')
    plt.ylabel('Error function Bi-210')
    plt.legend(loc=9)
    plt.grid(True)
    plt.show()

    fig2 = plt.figure()
    plt.plot(err_list[2], 'k', label='Difference between matrix and Runge-Kutta method for Po-210')
    plt.xlabel('Time [days]')
    plt.ylabel('Error function Po-210')
    plt.legend(loc=8)
    plt.grid(True)
    plt.show()

    return [fig0, fig1, fig2]


if __name__ == '__main__':
    plot_error_functions(err_list)