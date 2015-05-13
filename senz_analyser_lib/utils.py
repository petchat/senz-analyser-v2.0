import random
import scipy.stats as ss

def standardNormalRand(range_x, range_y):
    while True:
        X = random.uniform((-1)*range_x, range_x)
        Y = random.uniform(0.0, range_y)
        if Y < ss.norm.pdf(X):
            return abs(X)

def discreteSpecifiedRand(prob_dict_list):
    '''
    Discrete Specified Rand
    return a key which chosen from prob_dict_list in a specified discrete distribution.
    the input format look like:
        [{key: prob1}, {key: prob2}, ...]

    :param prob_dict_list:
    :return:
    '''
    rand  = random.random()
    # print 'rand is', rand
    scale = prob_dict_list[0].values()[0]
    index = 0
    while index <= len(prob_dict_list)-1:
        # print 'scale is', scale
        if rand <= scale:
            return prob_dict_list[index].keys()[0]
        elif rand > scale:
            index += 1
            scale += prob_dict_list[index].values()[0]

def chooseRandomly(choice_list):
    return random.choice(choice_list)

def selectOtherRandomly(prob_dict_list, universal_set):
    _universal_set = list(universal_set)
    # delete the existed keys from universal set
    for item in prob_dict_list:
        if item.keys()[0] is not 'Others':
            _universal_set.remove(item.keys()[0])
    # delete the key 'Others', and replace it by a new key which generated randomly
    index = 0
    while index < len(prob_dict_list):
        if prob_dict_list[index].keys()[0] is 'Others':
            prob_dict_list[index][random.choice(_universal_set)] = prob_dict_list[index].pop('Others')
        index += 1
    return prob_dict_list