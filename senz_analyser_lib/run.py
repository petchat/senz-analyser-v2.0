from hmmlearn.hmm import GMMHMM
from hmmlearn.hmm import GaussianHMM
from hmmlearn.hmm import MultinomialHMM
from sklearn.mixture.gmm import GMM
from datasets import Dataset
import numpy as np

# Prepare parameters for a 3-components HMM
# Initial population probability
start_prob = np.array([0.4, 0.3, 0.1, 0.2])
# The transition matrix, note that there are no transitions possible
# between component 1 and 4
trans_mat = np.array([[0.5, 0.2, 0.2, 0.1],
                      [0.3, 0.4, 0.2, 0.1],
                      [0.1, 0.2, 0.5, 0.2],
                      [0.2, 0.1, 0.1, 0.6]])

start_prob_prior = np.array([0.3, 0.3, 0.3, 0.1])

trans_mat_prior = np.array([[0.2, 0.1, 0.3, 0.4],
                            [0.3, 0.2, 0.2, 0.3],
                            [0.1, 0.1, 0.1, 0.7],
                            [0.1, 0.3, 0.4, 0.2]])

# Build an HMM instance and set parameters
model_dining  = GMMHMM(startprob_prior=start_prob_prior, transmat_prior=trans_mat_prior, startprob=start_prob, transmat=trans_mat, n_components=4, n_mix=4, covariance_type='spherical', n_iter=50)
model_fitness = GMMHMM(startprob_prior=start_prob_prior, transmat_prior=trans_mat_prior, startprob=start_prob, transmat=trans_mat, n_components=4, n_mix=10, covariance_type='spherical', n_iter=50)
model_work    = GMMHMM(startprob_prior=start_prob_prior, transmat_prior=trans_mat_prior, startprob=start_prob, transmat=trans_mat, n_components=4, n_mix=8, covariance_type='spherical', n_iter=50)
model_shop    = GMMHMM(startprob_prior=start_prob_prior, transmat_prior=trans_mat_prior, startprob=start_prob, transmat=trans_mat, n_components=4, n_mix=4, covariance_type='spherical', n_iter=50)

dataset_dining  = Dataset()
dataset_fitness = Dataset()
dataset_work    = Dataset()
dataset_shop    = Dataset()

obs_dining  = dataset_dining.randomObservations('dining_out_in_chinese_restaurant', 10, 30)
obs_fitness = dataset_fitness.randomObservations('running_fitness', 10, 30)
obs_work    = dataset_work.randomObservations('work', 10, 30)
obs_shop    = dataset_shop.randomObservations('shopping', 10, 30)
# dataset_dining.plotObservations3D()

D = Dataset(obs_dining).dataset
F = Dataset(obs_fitness).dataset
W = Dataset(obs_work).dataset
S = Dataset(obs_shop).dataset

print 'Before training'

print model_dining.startprob_
print model_dining.transmat_
print model_dining.gmms
print model_dining.covariance_type
print model_dining.covars_prior
# print model_dining.gmms_[0].covars_
# print model_dining.gmms_[0].means_
# print model_dining.gmms_[0].weights_

seq_d = dataset_dining.randomSequence('dining_out_in_chinese_restaurant', 10)
print 'dining:'
print seq_d
seq_f = dataset_fitness.randomSequence('running_fitness', 10)
print 'fitness'
print seq_f
seq_w = dataset_work.randomSequence('work', 10)
print 'work'
print seq_w
seq_s = dataset_shop.randomSequence('shopping', 10)
print 'shopping'
print seq_s

model_dining.fit(D)
model_fitness.fit(F)
model_work.fit(W)
model_shop.fit(S)


print model_dining.startprob_
print model_dining.transmat_


print 'After training'

print ' - Classification for model dining -'

print 'dining result:'
print model_dining.score(np.array(dataset_dining._convetNumericalSequence(seq_d)))
print 'fitness result'
print model_dining.score(np.array(dataset_fitness._convetNumericalSequence(seq_f)))
print 'work result'
print model_dining.score(np.array(dataset_fitness._convetNumericalSequence(seq_w)))
print 'shop result'
print model_dining.score(np.array(dataset_fitness._convetNumericalSequence(seq_s)))

print ' - Classification for model fitness -'

print 'dining result:'
print model_fitness.score(np.array(dataset_dining._convetNumericalSequence(seq_d)))
print 'fitness result'
print model_fitness.score(np.array(dataset_fitness._convetNumericalSequence(seq_f)))
print 'work result'
print model_fitness.score(np.array(dataset_fitness._convetNumericalSequence(seq_w)))
print 'shop result'
print model_fitness.score(np.array(dataset_fitness._convetNumericalSequence(seq_s)))

print ' - Classification for model work -'

print 'dining result:'
print model_work.score(np.array(dataset_dining._convetNumericalSequence(seq_d)))
print 'fitness result'
print model_work.score(np.array(dataset_fitness._convetNumericalSequence(seq_f)))
print 'work result'
print model_work.score(np.array(dataset_fitness._convetNumericalSequence(seq_w)))
print 'shop result'
print model_work.score(np.array(dataset_fitness._convetNumericalSequence(seq_s)))

print ' - Classification for model shopping -'

print 'dining result:'
print model_shop.score(np.array(dataset_dining._convetNumericalSequence(seq_d)))
print 'fitness result'
print model_shop.score(np.array(dataset_fitness._convetNumericalSequence(seq_f)))
print 'work result'
print model_shop.score(np.array(dataset_fitness._convetNumericalSequence(seq_w)))
print 'shop result'
print model_shop.score(np.array(dataset_fitness._convetNumericalSequence(seq_s)))

print model_dining.gmms
print model_dining.covariance_type
print model_dining.covars_prior
print model_dining.gmms_[0].covars_
print model_dining.gmms_[0].means_
print model_dining.gmms_[0].weights_

print model_dining.gmms_[1].covars_
print model_dining.gmms_[1].means_
print model_dining.gmms_[1].weights_

print model_dining.gmms_[2].covars_
print model_dining.gmms_[2].means_
print model_dining.gmms_[2].weights_

print model_dining.gmms_[3].covars_
print model_dining.gmms_[3].means_
print model_dining.gmms_[3].weights_

print len(model_dining.gmms_)

gmm = GMM(n_components=4, covariance_type='spherical', random_state=None, thresh=None, tol=1e-3, min_covar=1e-3, n_iter=100, n_init=1, params='wmc', init_params='wmc')
gmm.covars_  = model_dining.gmms_[0].covars_
gmm.means_   = model_dining.gmms_[0].means_
gmm.weights_ = model_dining.gmms_[0].weights_

