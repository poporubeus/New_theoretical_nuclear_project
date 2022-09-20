import matplotlib.pyplot as plt


def plot_rk(Polonium_problem):

    """
    Function that plots the result of Runge-Kutta method.

    Args:
        Polonium_problem.

    Returns:
        Figures : [fig0, fig1, fig2]

    """

    # Plot
    fig0 = plt.figure()
    plt.title('Bi-209')
    plt.plot(Polonium_problem[:, 0], 'r', label='Bismuth209')
    plt.xlabel('Time [days]')
    plt.ylabel('Bi209 concentration')
    plt.legend()
    plt.grid(True)
    plt.show()

    fig1 = plt.figure()
    plt.title('Bi-210')
    plt.plot(Polonium_problem[:, 1], 'b', label='Bismuth210')
    plt.xlabel('Time [days]')
    plt.ylabel('Bi210 concentration')
    plt.legend()
    plt.grid(True)
    plt.show()

    fig2 = plt.figure()
    plt.title('Po-210')
    plt.plot(Polonium_problem[:, 2], 'g', label='Polonium210')
    plt.xlabel('Time [days]')
    plt.ylabel('Po210 concentration')
    plt.legend()
    plt.grid(True)
    plt.show()

    return [fig0, fig1, fig2]