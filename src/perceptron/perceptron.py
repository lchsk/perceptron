class Perceptron(object):

    def __init__(self, data, settings):
        
        # Reference variables for Data and Settings
        self.data = data
        self.settings = settings

    def get_activation(self, item):
        '''Returns activation value.'''

        return sum([self.data.get_weight(word) for word in item])

    def sign(self, a):
        '''Returns 1 if <a> is positive, -1 otherwise.'''

        return 1 if a >= 0 else -1

    def _test(self, test_data, correct_label):
        '''Internal test function. Follows the pseudocode of the Perceptron algorithm.'''

        score = 0.0
        length = len(test_data)

        # Get each review in the test data
        for item in test_data:
            # <item> is a review, <item[0]> is a list of words
            a = self.get_activation(item[0])

            # This is a sign function compared to label. 
            # If prediction is correct, then increase score.
            # Used to be beautiful, like that: (1 if a >= 0 else -1) == correct_label, changed for readability
            if self.sign(a) == correct_label:
                score += 1

        return round(score * 100 / length, 3)

    def test(self):
        '''Runs _test function, prints and saves results to a file.'''

        
        if self.settings.params['test_training']:
            filename = 'training.txt'
            t1 = self.data.train_pos_list
            t2 = self.data.train_neg_list
        else:
            filename = 'test.txt'
            t1 = self.data.test_pos_list
            t2 = self.data.test_neg_list

        f = open(filename, 'a')

        # Run test!
        pos_pct = self._test(test_data=t1, correct_label=1)
        neg_pct = self._test(test_data=t2, correct_label=-1)

        # Take average
        overall = (pos_pct + neg_pct) / 2.0

        error = 100.0 - overall

        # This will be save into a file
        line = str(overall) + '\t' + str(error) + '\t' + str(self.settings.params['iterations']) + '\n'
        f.write(line)
        
        f.close()

        print 'Results (iterations: %d):' % self.settings.params['iterations']
        print 'Accuracy (positive dataset): %.3f %%' % pos_pct
        print 'Accuracy (negative dataset): %.3f %%' % neg_pct
        print 'Accuracy (overall): %.3f %%' % overall

    def train(self):
        '''Runs the training as many times as is wanted by the user. Shuffles data after each iteration.'''

        print '*' * 40
        print 'Training has started...'

        for i in xrange(0, self.settings.params['iterations']):
            self._train()

            # shuffles the training data, so that order does not matter
            self.data.shuffle()

        print 'Training has finished.'

    def _train(self):
        '''Actual training is done here. '''

        for item in self.data.train_list:
            # <item> is a review, <item[0] are words

            a = self.get_activation(item[0])

            # Multiply activation by label
            if a * item[1] <= 0:
                # Error here -> update weights
                self.data.update_weight(item)

    def _reset(self):
        '''Reset weights data, ie. assign 0 for each word in a dictionary.'''

        self.data.words = { k: 0 for k, v in self.data.words.iteritems() }

    def run(self):
        '''Top function to run everything. Runs the whole algorithm as 
            many times as user wants (<tests> parameter)'''

        for i in xrange(0, self.settings.params['tests']):

            self._reset()
            self.train()
            self.test()

            # Increase to check for different iteration.
            # So if iterations = 1, and tests = 50, whole program will be run for
            # every iteration from 1..50 (and results stored in a file)self.
            self.settings.params['iterations'] += 1