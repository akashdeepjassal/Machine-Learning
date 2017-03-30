
from multiprocessing import Process
from numpy import *
import time 
# y = mx + c
# m is slope, c is y-intercept
def compute_error_for_line_given_points(c, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + c)) ** 2
    return totalError / float(len(points))

def step_gradient(c_current, m_current, points, learningRate):
    c_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        c_gradient += -(2/N) * (y - ((m_current * x) + c_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + c_current))
    new_c = c_current - (learningRate * c_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_c, new_m]

def gradient_descent_runner(points, initial_c, initial_m, learning_rate, number_iterations):
    c = initial_c
    m = initial_m
    for i in range(number_iterations):
        c, m = step_gradient(c, m, array(points), learning_rate)
    return [c, m]

def run():
    start=time.time()
    points = genfromtxt("D1.csv", delimiter=",")
    learning_rate = 0.00001
    initial_c = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    number_iterations = 1000000
    print ("Starting with gradient descent at c = {0}, m = {1}, error = {2}".format(initial_c, initial_m, compute_error_for_line_given_points(initial_c, initial_m, points)))
    print ("Running...")
    [c, m] = gradient_descent_runner(points, initial_c, initial_m, learning_rate, number_iterations)
    print ("After {0} iterations c = {1}, m = {2}, error = {3}".format(number_iterations, c, m, compute_error_for_line_given_points(c, m, points)))
    end=time.time()
    total_time=end-start
    print("Time taken is {0}".format(total_time))
if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    p.join()
    