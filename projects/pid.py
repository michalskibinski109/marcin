from common.utils import get_logger
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, logger, dt, v, x, t):
        self.logger = logger
        self.x_end = x
        self.t_end = t
        self.t_l = []
        self.x_curr = []
        self.time = []
        self.dt = dt
        self.v = v

    def add_data(self, time, t, x):
        self.time.append(time)
        self.t_l.append(t)
        self.x_curr.append(x)

    def __call__(self):
        self.logger.info("Plotting data")
        plt.plot(self.time, self.t_l)
        plt.plot(self.time, self.x_curr)
        plt.scatter(self.time[-1], self.x_end, color="red", label="destination")
        plt.xlabel("Time")
        plt.legend(["estimated t", "x"])

        plt.show()


class Simulation:
    def __init__(
        self, v: float, dt: float, x_end: float, logger=get_logger(), error_rate=0.0
    ):
        self.t_end = 0.0
        self.t_l = 0.0
        self.x_curr = 0.0
        self.dt = dt
        self.v = v
        self.x_end = x_end
        self.logger = logger
        self.error_rate = error_rate
        self.plotter = Plotter(self.logger, self.dt, self.v, self.x_end, self.t_end)

    def __compute_time_left(self):
        if self.x_curr > self.x_end:
            return -1e-13
        return (self.x_end - self.x_curr) / self.v

    def __generate_error(self):
        e = np.random.random() * (self.v * self.error_rate)
        return e * (1 if np.random.random() > 0.5 else -1)

    def __call__(self):
        time = 0.0
        while self.t_l >= 0:
            time += self.dt
            self.t_l = self.__compute_time_left()
            error = self.__generate_error()
            self.x_dot = self.v + error
            self.x_curr += self.x_dot * self.dt
            self.logger.debug(
                f"time: {time * self.dt} t_l: {self.t_l:.3}, x_curr: {self.x_curr:.3}"
            )
            self.plotter.add_data(time * self.dt, self.t_l, self.x_curr)
        self.plotter()


simulation = Simulation(v=1, dt=0.001, x_end=0.1, error_rate=4)
simulation()
