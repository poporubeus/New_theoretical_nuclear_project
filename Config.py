class Decay:

    """
    Decay coefficients class:
        all the decay constants you need are collected here.

        Args:
            dBi209(float) : Bismuth209 decay constant;
            dBi210(float) : Bismuth210 decay constant;
            dPo210(float) : Polonium210 decay constant.

    """

    dBi209 = 1.83163e-12
    dBi210 = 1.60035e-6
    dPo210 = 5.79764e-8


class Init:

    """
    Initial concentrations class:
        initial nuclide concentrations inside this class.

        Args:
            Bi209_0(float) : Bismuth209 at initial time;
            Bi210_0(float) : Bismuth210 at initial time;
            Po210_0(float) : Polonium210 at initial time.

    """

    Bi209_0 = 6.95896e-4  # Initial Bismuth209
    Bi210_0 = 0.0  # Initial Bismuth210
    Po210_0 = 0.0  # Initial Polonium210


class Par:

    """
    Time class:
        parameters of the duration of the experiment.

        Args:
            total_time(int) : duration of the experiment
            time_step(int)  : increment

    """

    total_time = 365   # Days
    time_step = 86400  # Seconds