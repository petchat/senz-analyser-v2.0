from hmmlearn.hmm import GMMHMM
from hmmlearn.hmm import GaussianHMM
from hmmlearn.hmm import MultinomialHMM
from datasets import Dataset
import numpy as np

# Prepare parameters for a 3-components HMM
# Initial population probability
start_prob = np.array([0.6, 0.3, 0.1, 0.0])
# The transition matrix, note that there are no transitions possible
# between component 1 and 4
trans_mat = np.array([[0.7, 0.2, 0.0, 0.1],
                      [0.3, 0.5, 0.2, 0.0],
                      [0.0, 0.3, 0.5, 0.2],
                      [0.2, 0.0, 0.2, 0.6]])

# Build an HMM instance and set parameters
model_dining  = GMMHMM(startprob=start_prob, transmat=trans_mat, n_components=4, n_mix=4, covariance_type='spherical', n_iter=50)
model_fitness = GMMHMM(startprob=start_prob, transmat=trans_mat, n_components=4, n_mix=4, covariance_type='spherical', n_iter=50)

dataset_dining  = Dataset()
dataset_fitness = Dataset()

obs_dining  = dataset_dining.randomObservations('dining_out_in_chinese_restaurant', 10, 1000)
obs_fitness = dataset_fitness.randomObservations('running_fitness', 10, 1000)
dataset_dining.plotObservations3D()

D = Dataset(obs_dining).dataset
F = Dataset(obs_fitness).dataset

print 'Before training'

seq_d = dataset_dining.randomSequence('dining_out_in_chinese_restaurant', 10)
print 'dining:'
print seq_d
seq_f = dataset_fitness.randomSequence('running_fitness', 10)
print 'fitness'
print seq_f

model_dining.fit(D)
model_fitness.fit(F)

print 'After training'

print ' - Classification for model dining -'

print 'dining result:'
print model_dining.score(np.array(dataset_dining._convetNumericalSequence(seq_d)))
print 'fitness result'
print model_dining.score(np.array(dataset_fitness._convetNumericalSequence(seq_f)))

print ' - Classification for model fitness -'

print 'dining result:'
print model_fitness.score(np.array(dataset_dining._convetNumericalSequence(seq_d)))
print 'fitness result'
print model_fitness.score(np.array(dataset_fitness._convetNumericalSequence(seq_f)))