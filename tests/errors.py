from runge import u
from main import main
from Config import Par
import matplotlib.pyplot as plt
import numpy as np

u0 = u[:, 0]
u1 = u[:, 1]
u2 = u[:, 2]


mtx_expm0 = main(Par.total_time, Par.time_step)[:, 0]
mtx_expm1 = main(Par.total_time, Par.time_step)[:, 1]
mtx_expm2 = main(Par.total_time, Par.time_step)[:, 2]


err0 = mtx_expm0-u0
err1 = mtx_expm1-u1
err2 = mtx_expm2-u2
print(err0)
print(err1)
print(err2)


def plot_error_functions():
    fig0 = plt.figure()
    plt.plot(err0, 'k', label='Difference between matrix and Runge-Kutta method for Bi-209')
    plt.xlabel('Time [hours]')
    plt.ylabel('Error function Bi-209')
    plt.legend(loc=0)
    plt.grid(True)
    plt.show()

    fig1 = plt.figure()
    plt.plot(err1, 'k', label='Difference between matrix and Runge-Kutta method for Bi-210')
    plt.xlabel('Time [hours]')
    plt.ylabel('Error function Bi-210')
    plt.legend(loc=9)
    plt.grid(True)
    plt.show()

    fig2 = plt.figure()
    plt.plot(err2, 'k', label='Difference between matrix and Runge-Kutta method for Po-210')
    plt.xlabel('Time [hours]')
    plt.ylabel('Error function Po-210')
    plt.legend(loc=8)
    plt.grid(True)
    plt.show()

    fig3 = plt.figure()
    x = np.arange(0, len(err0))
    plt.scatter(x, err0, c='blue')
    plt.grid(True)
    plt.show()

    fig4 = plt.figure()
    x = np.arange(0, len(err1))
    plt.scatter(x, err1, c='green')
    plt.grid(True)
    plt.show()

    fig5 = plt.figure()
    x = np.arange(0, len(err2))
    plt.scatter(x, err2, c='purple')
    plt.grid(True)
    plt.show()

    return [fig0, fig1, fig2, fig3, fig4, fig5]


if __name__ == '__main__':
    plot_error_functions()