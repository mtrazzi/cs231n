import os
import pickle
import numpy as np


def grep_form_path(path, to_grep):
    return [fn for fn in os.listdir(path) if to_grep in fn]


def load_file(fn):
    with open(fn, 'rb') as f:
        bob = pickle.load(f, encoding='bytes')
    return bob


def load_batch(path, batch_id):
    return load_file(os.path.join(path, batch_id))


def load_cifar():
    prefix = '.' if os.path.isdir("./data") else '..'
    path = prefix + '/data/cifar-10-batches-py'
    train = grep_form_path(path, "data")
    test = grep_form_path(path, "test")
    dicts_train = [load_batch(path, train_file) for train_file in train]
    dicts_test = [load_batch(path, test_file) for test_file in test]
    Xtrainl, Ytrainl = zip(*[(d[b'data'], d[b'labels']) for d in dicts_train])
    Xtestl, Ytestl = zip(*[(d[b'data'], d[b'labels']) for d in dicts_test])
    def concat(datal): return np.concatenate([data for data in datal], axis=0)
    Xtrain, Ytrain, Xtest, Ytest = map(concat,
                                       [Xtrainl, Ytrainl, Xtestl, Ytestl])
    return Xtrain, Ytrain, Xtest, Ytest


if __name__ == '__main__':
    load_cifar()
