from perceptron.perceptron import Perceptron
from perceptron.data import Data


if __name__ == '__main__':

    data = Data(
        directory='../data/', 
        train_pos='train.positive', 
        train_neg='train.negative', 
        test_pos='test.positive', 
        test_neg='test.negative'
        )

    p = Perceptron(data)

    # print data.words['fantastic']
    for i in xrange(0, 50):
        p.train()
    p.test()
    # print data.words

    i = 0
    for k, v in data.words.iteritems():

        if v[1] != 0:
            # print k, v
            i+=1
    # print i
    # print len(data.words)