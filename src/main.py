from perceptron.perceptron import Perceptron
from perceptron.data import Data
from perceptron.settings import Settings

if __name__ == '__main__':

    settings = Settings()
    settings.read_parameters()
    settings.print_parameters()

    # initiate data object
    # and set filesnames to the ones given
    data = Data(
        directory='../data/', 
        train_pos='train.positive', 
        train_neg='train.negative', 
        test_pos='test.positive', 
        test_neg='test.negative'
        )

    # create a Perceptron object and run it!
    p = Perceptron(data, settings)
    p.run()