from main import main
import numpy as np
from tabulate import tabulate
from Config import *
from runge import rk_method, ode_system, u0


def Table_of_results():

    """
        Function that collects tables where results of different methods are printed.

        In the table1 there are nuclide concentrations calculated with matrix exponential method and the time.

        Args:
            No args.

        Returns:
            tables: table1, table2
    """

    result_matrix = main(Par.total_time, Par.time_step)    # Recalling main function in order to compute the result of
    # matrix exponential method

    result_rk4 = rk_method(ode_system, u0, Par.time_step, Par.total_time)   # Recalling the rk_method in order to
    # compute the result of Runge-Kutta algorithm

    # Creating empty lists for the three concentrations twice for each method
    matrix1 = []
    matrix2 = []
    matrix3 = []

    rk1 = []
    rk2 = []
    rk3 = []

    # Initialize the time vector
    time = np.arange(0, 365)

    # Initialize empty tables: table1 contains matrix expm, while table2 does RungeKutta
    table1 = []
    table2 = []

    for i in range(len(time)):

        # appending only the component of the nuclide concentrations and collecting into the previous lists
        matrix1.append(result_matrix[i][0])
        matrix2.append(result_matrix[i][1])
        matrix3.append(result_matrix[i][2])
        rk1.append(result_rk4[i][0])
        rk2.append(result_rk4[i][1])
        rk3.append(result_rk4[i][2])

        # Updating the tables: notice they contain time in the first columns
        table1.append([i, matrix1[i], matrix2[i], matrix3[i]])
        table2.append([i, rk1[i], rk2[i], rk3[i]])

    # Print tables
    print('Table of nuclide concentrations calculated with matrix expm')
    print('')
    print(tabulate(table1, headers=['Time', 'Bi209', 'Bi210', 'Po210']))
    print('')
    print('Table of nuclide concentrations calculated with Runge-Kutta')
    print('')
    print(tabulate(table2, headers=['Time', 'Bi209', 'Bi210', 'Po210']))

    return table1, table2


if __name__ == '__main__':
    Table_of_results()