import matplotlib.pyplot as plt


def plot(Polonium_problem):

    """
    Function that collects all the plot graphs.

    Returns:
        [fig0, fig1, fig2] : array that shows the three graphs for the concentrations.

    """
    fig0 = plt.figure()
    plt.title('Matrix exponential method for Bi209')
    plt.xlabel('Time [days]')
    plt.ylabel('Nuclide concentration')
    plt.plot(Polonium_problem[:, 0], 'r', label='Bismuth209')
    plt.legend()
    plt.grid(True)

    plt.savefig('Bismuth-209.png')

    fig1 = plt.figure()
    plt.title('Matrix exponential method for Bi210')
    plt.xlabel('Time [days]')
    plt.ylabel('Nuclide concentration')
    plt.plot(Polonium_problem[:, 1], 'b', label='Bismuth210')
    plt.legend()
    plt.grid(True)

    plt.savefig('Bismuth-210.png')

    fig2 = plt.figure()
    plt.title('Matrix exponential method for Po210')
    plt.xlabel('Time [days]')
    plt.ylabel('Nuclide concentration')
    plt.plot(Polonium_problem[:, 2], 'g', label='Polonium210')
    plt.legend()
    plt.grid(True)

    plt.savefig('Polonium-210.png')

    plt.show()

    return [fig0, fig1, fig2]

