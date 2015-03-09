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

        self.train_list = []
        self.test_pos_list = []
        self.test_neg_list = []

        self.words = {}

        self.load()

    def get_weight(self, word):
        return self.words[word]

    def update_weight(self, item):

        words = item[0]
        label = item[1]

        for word in words:
            self.words[word] = self.words[word] + label

    def _load(self, filename, label, target_obj):

        f = open(self.dir + filename, 'r')
        loaded = []

        for line in f:

            instance = []
            features = []

            for x in line.strip().split():
                features += [x]

                if x not in self.words:
                    # label (1, -1), weight
                    # self.words[x] = [label, 0]
                    self.words[x] = 0

            instance.append(features)
            instance.append(label)

            loaded += [instance]

        f.close()
        target_obj += loaded

    def load(self):
        self._load(self.train_pos, 1, self.train_list)
        self._load(self.train_neg, -1, self.train_list)

        self._load(self.test_pos, 1, self.test_pos_list)
        self._load(self.test_neg, -1, self.test_neg_list)

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.train_list)

