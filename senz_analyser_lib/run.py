from hmmlearn.hmm import GMMHMM
from datasets import Dataset

seq = Dataset.eating_seq_sample
# Build an HMM instance and set parameters
model = GMMHMM(4, n_mix=3, covariance_type='diag')
print 'start prob'
print model.startprob_
print 'trans mat'
print model.transmat_

print model.fit([seq])

print 'start prob'
print model.startprob_
print 'trans mat'
print model.transmat_
