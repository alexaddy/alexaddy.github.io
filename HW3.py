import numpy as np
import scipy.stats
 
# one coin has a probability of coming up heads of 0.2, the other 0.6
coinProbs = np.zeros (2)
coinProbs[0] = 0.2
coinProbs[1] = 0.6
 
# reach in and pull out a coin numTimes times
numTimes = 100
 
# flip it numFlips times when you do
numFlips = 2
 
# flips will have the number of heads we observed in 10 flips for each coin
flips = np.zeros (numTimes)
for coin in range(numTimes):
    which = np.random.binomial (1, 0.5, 1);
    flips[coin] = np.random.binomial (numFlips, coinProbs[which], 1);
 
# initialize the EM algorithm
coinProbs[0] = 0.79
coinProbs[1] = 0.51

# probability that a coin is z given the x flips and the stored parameters
def c(coin, numHeads, count):
	numerator = 0.5 * scipy.stats.binom.pmf(numHeads, count, coinProbs[coin])
	denominator = (0.5 * scipy.stats.binom.pmf(numHeads, count, coinProbs[0])) + (0.5 * scipy.stats.binom.pmf(numHeads, count, coinProbs[1]))
	return np.divide(numerator, denominator)
 
# run the EM algorithm
c0 = np.zeros(numTimes)
c1 = np.zeros(numTimes)

for iters in range (20):
	for c_iter in range(numTimes):
		c0[c_iter] = c(0, flips[c_iter], numFlips)
		c1[c_iter] = c(1, flips[c_iter], numFlips)

	# print flips
	# print c0
	# print np.sum(np.multiply(flips, c0))

	# print np.sum(np.multiply(10, c0))

	coinProbs[0] = np.divide(np.sum(np.multiply(c0, flips)), np.sum(np.multiply(c0, numFlips)))
	coinProbs[1] = np.divide(np.sum(np.multiply(c1, flips)), np.sum(np.multiply(c1, numFlips)))

	print coinProbs
