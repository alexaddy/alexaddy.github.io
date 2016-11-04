import numpy as np
import math

# Homework 2

def f (x, y):
	return math.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1

def f_grad(a):
	return np.array([math.cos(a[0] + a[1]) + 2*(a[0] - a[1]) - 1.5,
		math.cos(a[0] + a[1]) - 2*(a[0] - a[1]) + 2.5])

def f_hess(a):
	return np.array([[-math.sin(a[0] + a[1]) + 2, -math.sin(a[0] + a[1]) - 2],
		[-math.sin(a[0] + a[1]) - 2, -math.sin(a[0] + a[1]) + 2]])

def gd_optimize(a):
	theta_last = np.zeros(2)
	theta = a

	l = 1

	while np.linalg.norm(np.subtract(theta, theta_last), 1) > 10**(-20):
		theta_last = theta
		theta = np.subtract(theta_last, np.multiply(l, f_grad(theta_last)))

		print f(theta[0], theta[1])

		# Driving boldly
		if f(theta[0], theta[1]) < f(theta_last[0], theta_last[1]):
			l *= 1.1
		else:
			l *= 0.5

	return theta

def nm_optimize(a):
	theta_last = np.zeros(2)
	theta = a

	while not np.array_equal(theta, theta_last):
		theta_last = theta
		theta = theta - np.dot(np.linalg.inv(f_hess(theta)), f_grad(theta))

		print f(*theta)

	return theta


print gd_optimize(np.array([-0.2, -1.0]))
print 
print gd_optimize (np.array ([-0.5, -1.5]))
print
print nm_optimize (np.array ([-0.2, -1.0]))
print
print nm_optimize (np.array ([-0.5, -1.5]))