import random

class Data(object):

    def __init__(self, directory, train_neg, train_pos, test_neg, test_pos):
        
        # Directory in which data files are located
        self.dir = directory

        # Filenames of data files
        self.train_neg = train_neg
        self.train_pos = train_pos
        self.test_neg = test_neg
        self.test_pos = test_pos

        # All training data
        self.train_list = []

        # Separate lists for positive and negative training data
        self.train_pos_list = []
        self.train_neg_list = []

        # Test data (positive)
        self.test_pos_list = []

        # Test data (negative)
        self.test_neg_list = []

        # Dictionary that holds words (key) and weights (value)
        self.words = {}

        # we run loading of the data already in the constructor
        self.load()

    def get_weight(self, word):
        '''Simply returns weight of a given word'''

        return self.words[word]

    def update_weight(self, item):
        '''Update weights for all words in a given review.
            Review (item) is stored as a list which consists of two elements:
            1) all words from the review
            2) label (1 or -1)
        '''

        words = item[0]
        label = item[1]

        for word in words:
            self.words[word] = self.words[word] + label

    def _load(self, filename, label, target_obj):
        '''Loads data. It might look a bit weird, 
            but the point is that I wanted to have a structure like this:
            [words, label], where <words> is a list and label is a number, so it could
            be address by indexing (zeroth element: list of words, first element: label).
        '''

        f = open(self.dir + filename, 'r')
        loaded = []

        for line in f:

            # Here <line> is essentially a review

            instance = []
            features = []

            for x in line.strip().split():
                features += [x]

                # Here a dictionary with all the words is built
                # In a dictionary keys are unique, so there's no need
                # to work with sets etc.
                self.words[x] = 0

            instance.append(features)
            instance.append(label)

            loaded += [instance]

        f.close()
        target_obj += loaded

    def load(self):
        '''External method for loading the data. Points to correct files, variables and assigns labels.'''

        self._load(self.train_pos, 1, self.train_pos_list)
        self._load(self.train_neg, -1, self.train_neg_list)

        # Combine two training sets into one
        self.train_list = self.train_pos_list + self.train_neg_list

        self._load(self.test_pos, 1, self.test_pos_list)
        self._load(self.test_neg, -1, self.test_neg_list)

        # remember to shuffle so that the order is random
        self.shuffle()

    def shuffle(self):
        '''Shuffles a training list. Should be called after each iteration.'''
        
        random.shuffle(self.train_list)

