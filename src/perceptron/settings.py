import sys
import getopt

class Settings(object):
    def __init__(self):

        # Parameters dictionary
        self.params = {}

        # Number of iterations to perform
        self.params['iterations'] = 1

    def help(self):
        print 'Help...'
        sys.exit(0)

    def read_parameters(self):
        opts, args = getopt.getopt(sys.argv[1:], "hi:", ['help', 'iterations'])

        try:
            for opt, arg in opts:
                if opt in ("-H", "--help"):
                    self.help()
                elif opt in ('-i', '--iterations'):
                    self.params['iterations'] = int(arg)

                else:
                    self.help()
            
        except getopt.GetoptError:
            self.help()

    def print_parameters(self):
        print 'Parameters:'
        for k, v in self.params.iteritems():
            print '\t' + k + ': ' + str(v)

        print '*' * 50