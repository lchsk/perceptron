import sys
import getopt

class Settings(object):
    def __init__(self):

        # Parameters dictionary
        self.params = {}

        # Number of iterations to perform
        self.params['iterations'] = 1

        # How many tests should be run
        # after each test <iterations> parameter is incremented
        self.params['tests'] = 1

        # If set to True when program is run
        # training data will be tested (and will give 100% accuracy!)
        self.params['test_training'] = False

    def help(self):
        '''Prints help information, explains all the parameters'''

        print 'This program implements the perceptron algorithm, which in this case '
        print 'classifies amazon reviews into positive or negative ones.'
        print 'Usage:'
        print '\t-h\tfor help'
        print '\t-i <int>\tnumber of iterations'
        print '\t-t <int>\tnumber of tests'
        print '\t-T\tif set, training data will be tested (and not test data)'

        sys.exit(0)

    def read_parameters(self):
        '''Reads parameters from the command line and sets corresponding variables'''

        opts, args = getopt.getopt(sys.argv[1:], "hi:t:T", ['help', 'iterations', 'tests', 'training'])

        try:
            for opt, arg in opts:
                if opt in ("-h", "--help"):
                    self.help()
                elif opt in ('-i', '--iterations'):
                    self.params['iterations'] = int(arg)
                elif opt in ('-t', '--tests'):
                    self.params['tests'] = int(arg)
                elif opt in ('-T', '--training'):
                    # If it is set to true, then we are going to test against the training data(!)
                    self.params['test_training'] = True
                else:
                    self.help()
            
        except getopt.GetoptError:
            self.help()

    def print_parameters(self):
        '''Prints parameters to the user to make sure that they were read properly'''

        print 'Parameters:'
        for k, v in self.params.iteritems():
            print '\t' + k + ': ' + str(v)

        print '*' * 50