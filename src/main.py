from perceptron.perceptron import Perceptron
from perceptron.data import Data
from perceptron.settings import Settings


if __name__ == '__main__':

    settings = Settings()
    settings.read_parameters()
    settings.print_parameters()

    data = Data(
        directory='../data/', 
        train_pos='train.positive', 
        train_neg='train.negative', 
        test_pos='test.positive', 
        test_neg='test.negative'
        )

    p = Perceptron(data, settings)

    p.train()
    p.test()

    # i = 0
    # for k, v in data.words.iteritems():

    #     if v != 0:
    #         # print k, v
    #         i+=1
    # print i
    # print len(data.words)